📊 Análise Financeira do Setor Bancário

Dashboard interativo desenvolvido em Python e Streamlit para analisar e comparar o desempenho histórico de cinco instituições financeiras brasileiras por meio de indicadores estatísticos e visualizações financeiras.

O projeto utiliza dados históricos de mercado para explorar a evolução das cotações, rentabilidade e volatilidade das ações, permitindo comparações entre os bancos e diferentes períodos de análise.

🏦 Instituições analisadas

Instituição| Código
Itaú Unibanco| ITUB4
Bradesco| BBDC4
Banco do Brasil| BBAS3
Santander| SANB11
BTG Pactual| BPAC11

📈 Funcionalidades

- Seleção individual ou conjunta das instituições financeiras.
- Filtro interativo por período de análise.
- Acompanhamento da evolução histórica das cotações.
- Cálculo de rentabilidade percentual.
- Cálculo de volatilidade anualizada.
- Identificação dos maiores e menores preços.
- Comparação do melhor e pior desempenho.
- Análise de risco e retorno por meio de gráfico de dispersão.
- Indicadores financeiros apresentados em cartões.
- Gráficos comparativos de rentabilidade e volatilidade.

🖥️ Demonstração do dashboard

1. Indicadores de rentabilidade

Apresentação dos indicadores de rentabilidade das ações selecionadas.

"Indicadores de rentabilidade" (imagens/analise_bancaria/indicadores_rentabilidade.png)

2. Indicadores de volatilidade e preços

Comparação da volatilidade das ações e identificação dos maiores e menores preços.

"Indicadores de volatilidade e preços" (imagens/analise_bancaria/indicadores_volatilidade_precos.png)

3. Evolução das cotações e análise de risco e retorno

Visualização do comportamento histórico das ações e comparação entre rentabilidade e volatilidade.

"Evolução das cotações e risco e retorno" (imagens/analise_bancaria/evolucao_e_risco_retorno.png)

4. Comparativo de rentabilidade e volatilidade

Comparação visual do desempenho das cinco instituições financeiras.

"Comparativo de rentabilidade e volatilidade" (imagens/analise_bancaria/comparativo_rentabilidade_volatilidade.png)

🛠️ Tecnologias utilizadas

Tecnologia| Aplicação
Python| Desenvolvimento e processamento
Pandas| Manipulação e análise de dados
Streamlit| Desenvolvimento do dashboard interativo
yfinance| Obtenção de cotações históricas

📡 Fonte dos dados

Os dados históricos das ações são obtidos por meio do Yahoo Finance, utilizando a biblioteca "yfinance".

Período de análise configurado: janeiro de 2020 a dezembro de 2026.

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
│   └── analise_bancaria/
│       ├── indicadores_rentabilidade.png
│       ├── indicadores_volatilidade_precos.png
│       ├── evolucao_e_risco_retorno.png
│       └── comparativo_rentabilidade_volatilidade.png
│
├── .gitignore
├── README.md
└── requirements.txt

⚙️ Como executar o projeto

1. Clonar o repositório

git clone https://github.com/gabriel-angelo-021/analise_financeira_setor_bancario.git

2. Entrar na pasta do projeto

cd projeto_analise_financeira

3. Criar o ambiente virtual

python -m venv .venv

4. Ativar o ambiente virtual

Windows PowerShell:

.\.venv\Scripts\Activate.ps1

5. Instalar as dependências

python -m pip install -r requirements.txt

6. Executar o dashboard

python -m streamlit run .\deshboard\app.py

Após a execução, o Streamlit disponibilizará a aplicação no navegador.

🎯 Objetivo do projeto

Aplicar conhecimentos de programação, manipulação de dados, estatística e visualização de informações financeiras em um projeto prático de portfólio, desenvolvendo uma ferramenta interativa para análise comparativa do setor bancário brasileiro.

⚠️ Aviso

Este projeto possui finalidade educacional e de portfólio. Os resultados apresentados não constituem recomendações de investimento.