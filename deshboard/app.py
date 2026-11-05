
import os
import unicodedata
from datetime import datetime
import pandas as pd
import streamlit as st
import yfinance as yf

# funções de carregamento de dados de ITUB4 , BBDC4, BBAS3, SANB11 e BPAC11
     # a análise de desempenho serar de 2020 até 2026
@st.cache_data
def carregar_dados(empresas):
    texto_tickers = " ".join(empresas)
    dados_acao = yf.Tickers(texto_tickers)
    cotacoes_acao = dados_acao.history( start='2020-01-01', end='2026-12-31')
    cotacoes_acao = cotacoes_acao["Close"]
    cotacoes_acao = cotacoes_acao.rename(columns={
    "ITUB4.SA": "Itaú Unibanco",
    "BBDC4.SA": "Bradesco",
    "BBAS3.SA": "Banco do Brasil",
    "SANB11.SA": "Santander",
    "BPAC11.SA": "BTG Pactual"
    })
    return cotacoes_acao

acoes = ['ITUB4.SA', 'BBDC4.SA', 'BBAS3.SA', 'SANB11.SA', 'BPAC11.SA']
# preparo dos visualizações
dados = carregar_dados(acoes)

# criar a interfaca do stremilit
st.write('''
# Análise automatizada do desempenho dos bancos:
Acompanhe cotações, rentabilidade, volatilidade, evolução histórica e indicadores estatísticos, com comparações e identificação dos melhores e piores desempenhos do setor bancário.
''') # markdown

# prepara as visualizações = filtros lateral
st.sidebar.header("Filtros")

# preparo dos visualizações = filtros
lista_acoes = st.sidebar.multiselect("Selecione as ações:", dados.columns)
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica: "Close"})

# filtro de dados por data
data_inicial = dados.index.min().to_pydatetime()
data_final = dados.index.max().to_pydatetime()
intervalo_data = st.sidebar.slider("Selecione o periodo de analise:", min_value=data_inicial, max_value=data_final, value=(data_inicial, data_final))
dados = dados.loc[intervalo_data[0]:intervalo_data[1]]

# preparo dos dados de rentabilidade
rentabilidade = ((dados.iloc[-1] / dados.iloc[0]) - 1) * 100
rentabilidade = rentabilidade.round(2)

# preparo dos dados de volatilidade
retornos_diarios = dados.pct_change()
volatilidade = retornos_diarios.std() * (252 ** 0.5) * 100
volatilidade = volatilidade.round(2)

# preparo dos indicadores estatisticos
preco_medio = dados.mean().round(2)
preco_maximo = dados.max().round(2)
preco_minimo = dados.min().round(2)
desvio_padrao = dados.std().round(2)

# comparacao de desempenho entre os bancos
melhor_desempenho = rentabilidade.idxmax()
pior_desempenho = rentabilidade.idxmin()

# analise automatica
print("ANÁLISE AUTOMÁTICA")
print("==============================")
print(f"Melhor desempenho: {melhor_desempenho} ({rentabilidade[melhor_desempenho]}%)")
print(f"Pior desempenho: {pior_desempenho} ({rentabilidade[pior_desempenho]}%)")
print("==============================")

st.divider()
# indicadores de rentabilidade
st.subheader("Rentabilidade das ações")
colunas = st.columns(len(rentabilidade))
for coluna, (banco, valor) in zip(colunas, rentabilidade.items()):
    with coluna:
        st.metric(
            label=banco,
            value=f"{valor:.2f}%",
            delta=f"{valor:.2f}%",
            border=True
        )
# indicadores de volatilidade
st.subheader("Volatilidade das ações")
colunas = st.columns(len(volatilidade))
for coluna, (banco, valor) in zip(colunas, volatilidade.items()):
    with coluna:
        st.metric(
            label=banco,
            value=f"{valor:.2f}%",
            delta=f"{valor:.2f}%",
            delta_color="inverse",
            border=True
        )

# indicadores de maior e menor preco
st.subheader("Preços das ações")
coluna1, coluna2 = st.columns(2)
with coluna1:
    st.metric("Maior preço", f"R$ {preco_maximo.max():.2f}")
with coluna2:
    st.metric("Menor preço", f"R$ {preco_minimo.min():.2f}")

 # grafico de evolução historica das ações
st.subheader("Evolução histórica das ações")
st.line_chart(dados)
st.caption("Evolução das cotações de fechamento dos bancos selecionados no período analisado.")

# graficos comparativos
coluna1, coluna2 = st.columns(2)
# grafico de rentabilidade
with coluna1:
    st.subheader("Rentabilidade por banco")
    st.bar_chart(rentabilidade)
    st.caption("Variação percentual das ações no período selecionado.")
# grafico de volatilidade
with coluna2:
    st.subheader("Volatilidade por banco")
    st.bar_chart(volatilidade)
    st.caption("Volatilidade anualizada das ações no período selecionado.")
st.divider()
st.caption(
    "Fonte dos dados: Yahoo Finance | "
    "Projeto desenvolvido em Python e Streamlit."
)
st.caption(
    "Análise para fins educacionais e informativos. "
    "Não constitui recomendação de investimento."
)