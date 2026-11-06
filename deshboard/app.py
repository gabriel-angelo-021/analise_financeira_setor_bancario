import pandas as pd
import streamlit as st
import yfinance as yf


# funções de carregamento de dados de ITUB4 , BBDC4, BBAS3, SANB11 e BPAC11
     # a análise de desempenho serar de 2020 até 2026
st.set_page_config(
    page_title="Desempenho do Mercado",
    page_icon="📊",
    layout="wide"
)

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
st.subheader("Análise automática de desempenho")
coluna1, coluna2 = st.columns(2)
with coluna1:
    st.metric(
        "Melhor desempenho",
        melhor_desempenho,
        f"{rentabilidade[melhor_desempenho]:.2f}%"
    )
with coluna2:
    st.metric(
        "Pior desempenho",
        pior_desempenho,
        f"{rentabilidade[pior_desempenho]:.2f}%"
    )

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
banco_maior_preco = preco_maximo.idxmax()
banco_menor_preco = preco_minimo.idxmin()
coluna1, coluna2 = st.columns(2)
with coluna1:
    st.metric(
        f"Maior preço — {banco_maior_preco}",
        f"R$ {preco_maximo[banco_maior_preco]:.2f}"
    )
with coluna2:
    st.metric(
        f"Menor preço — {banco_menor_preco}",
        f"R$ {preco_minimo[banco_menor_preco]:.2f}"
    )
# Graficosb de evolução histórica e comparativo com base 100
col1, col2 = st.columns(2, gap="large")

# Gráfico de evolução histórica
with col1:
    st.subheader("Evolução das cotações")
    st.line_chart(
        dados,
        height=420,
        use_container_width=True
    )

# Gráfico de dispersão — risco e retorno
with col2:
    st.subheader("Análise de risco e retorno")
    dados_dispersao = pd.DataFrame({
        "Banco": rentabilidade.index.astype(str),
        "Volatilidade": volatilidade.values,
        "Rentabilidade": rentabilidade.values
    })
    st.scatter_chart(
        dados_dispersao,
        x="Volatilidade",
        y="Rentabilidade",
        color="Banco",
        height=420
    )

# graficos comparativos
coluna1, coluna2 = st.columns(2)

# grafico de rentabilidade
with coluna1:
    st.subheader("Rentabilidade por banco")
    grafico_rentabilidade = rentabilidade.rename_axis("Banco").reset_index(name="Rentabilidade")
    st.bar_chart(
        grafico_rentabilidade,
        x="Banco",
        y="Rentabilidade",
        color="Banco"
    )
   
# grafico de volatilidade
with coluna2:
    st.subheader("Volatilidade por banco")
    grafico_volatilidade = volatilidade.rename_axis("Banco").reset_index(name="Volatilidade")
    st.bar_chart(
        grafico_volatilidade,
        x="Banco",
        y="Volatilidade",
        color="Banco"
    )