📊 Análise Financeira do Setor Bancário

Dashboard interativo desenvolvido em Python e Streamlit para analisar e comparar o desempenho das ações de cinco dos principais bancos brasileiros.

O projeto transforma dados históricos do mercado financeiro em indicadores e visualizações que facilitam a análise de rentabilidade, volatilidade e evolução das cotações.

🏦 Instituições analisadas

Instituição| Código da ação
Itaú Unibanco| ITUB4
Bradesco| BBDC4
Banco do Brasil| BBAS3
Santander| SANB11
BTG Pactual| BPAC11

📈 Funcionalidades

- Seleção individual ou conjunta dos bancos.
- Filtro por período de análise.
- Acompanhamento histórico das cotações.
- Cálculo de rentabilidade.
- Cálculo de volatilidade anualizada.
- Identificação dos maiores e menores preços.
- Comparação de desempenho entre instituições.
- Indicadores financeiros apresentados em cartões.
- Gráficos para facilitar a análise comparativa.

🖥️ Demonstração do dashboard

Visão geral

"Visão geral do dashboard" (imagens/deshbord.geral.png)

Comparativo: Itaú Unibanco e Santander

"Comparativo Itaú e Santander" (imagens/comparativo_itau_santander.png)

Comparativo: Banco do Brasil, Bradesco e BTG Pactual

"Comparativo Banco do Brasil, Bradesco e BTG Pactual" (imagens/comparativo_bb_bradesco_btg.png)

🛠️ Tecnologias utilizadas

- Python: desenvolvimento e processamento.
- Streamlit: construção da interface interativa.
- Pandas: tratamento e análise dos dados.
- yfinance: obtenção das cotações históricas.

📡 Fonte dos dados

Os dados históricos das ações são obtidos por meio do Yahoo Finance, utilizando a biblioteca "yfinance".

📁 Estrutura do projeto

projeto_analise_financeira/
│
├── .streamlit/
│   └── config.toml
│
├── deshboard/
│   └── app.py
│
├── imagens/
│   ├── deshbord.geral.png
│   ├── comparativo_itau_santander.png
│   └── comparativo_bb_bradesco_btg.png
│
├── .gitignore
├── README.md
└── requirements.txt

⚙️ Como executar o projeto

1. Clonar o repositório

git clone URL_DO_SEU_REPOSITORIO

2. Entrar na pasta do projeto

cd projeto_analise_financeira

3. Criar o ambiente virtual

python -m venv .venv

4. Ativar o ambiente virtual

No Windows PowerShell:

.\.venv\Scripts\Activate.ps1

5. Instalar as dependências

python -m pip install -r requirements.txt

6. Executar o dashboard

python -m streamlit run .\deshboard\app.py

Após executar o comando, o Streamlit disponibilizará o dashboard no navegador.

🎯 Objetivo do projeto

Aplicar conhecimentos de programação, análise de dados e visualização de informações financeiras em um projeto prático de portfólio, explorando indicadores e comparações entre instituições do setor bancário brasileiro.

⚠️ Aviso

Este projeto possui finalidade educacional e de portfólio. As análises apresentadas não constituem recomendações de investimento.