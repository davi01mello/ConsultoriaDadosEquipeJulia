Markdown

<br />
<p align="center">
  <a href="https://github.com/CITi-UFPE/PTA-ciencia-de-dados">
    <img src="https://github.com/CITi-UFPE.png" alt="Logo" width="180px">
  </a>

  <h3 align="center">O-Market Data Solutions</h3>
  <h4 align="center">Consultoria de Dados e Inteligência Estratégica</h4>

  <p align="center">
   Este projeto foi desenvolvido durante o Processo de Treinamento de Área (PTA) do CITi, com foco na transformação de dados brutos em inteligência de negócio. A solução abrange Engenharia de Dados, Ciência de Dados (Agentes de IA) e Business Intelligence.
    <br />
    <a href="https://github.com/CITi-UFPE/PTA-ciencia-de-dados"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/CITi-UFPE/PTA-ciencia-de-dados/issues">Report Bug</a>
    ·
    <a href="https://github.com/CITi-UFPE/PTA-ciencia-de-dados/issues">Request Feature</a>
  </p>
</p>

<details open="open">
  <summary><h2 style="display: inline-block">Tabela de Conteúdo</h2></summary>
  <ol>
    <li><a href="#sobre-o-projeto">Sobre o Projeto</a></li>
    <li><a href="#objetivos-da-consultoria">Objetivos da Consultoria</a></li>
    <li><a href="#tecnologias-utilizadas">Tecnologias Utilizadas</a></li>
    <li><a href="#como-instalar">Como Instalar</a></li>
    <li><a href="#como-rodar-a-análise">Como Rodar a Análise</a></li>
    <li><a href="#insights-gerados">Insights Gerados</a></li>
    <li><a href="#contato">Contato</a></li>
  </ol>
</details>

<br/>

## Sobre o Projeto
<br/>

O projeto O-Market simula um cenário real de consultoria de dados para um e-commerce. Nas primeiras fases, construímos um Data Warehouse robusto e Agentes de IA. Nesta fase final, atuamos como consultores estratégicos, utilizando esses dados para diagnosticar gargalos operacionais, ineficiências financeiras e propor um plano de expansão.

A solução entrega não apenas código, mas valor de negócio tangível através de dashboards interativos e planos de ação baseados em dados.

<br/>

## Objetivos da Consultoria
<br/>

1.  **Monitoramento:** Criação de um painel de controlo (Dashboard) para acompanhar a saúde da operação em tempo real.
2.  **Diagnóstico:** Identificação de onde a empresa perde dinheiro (cancelamentos, frete abusivo, atrasos).
3.  **Plano de Ação:** Proposta de soluções baseadas em dados para estancar as perdas e acelerar o crescimento.

<br/>

## Tecnologias Utilizadas
<br/>

* **Linguagem:** Python 3.10+
* **Análise de Dados:** Pandas, NumPy
* **Visualização:** Power BI / Looker Studio
* **Engenharia:** FastAPI, n8n, Ngrok
* **Banco de Dados:** Supabase (PostgreSQL)

<br/>

## Como Instalar
<br/>

1. Certifique-se de que o **Python** e o **Git** estão instalados na sua máquina.

2. Clone o repositório:

   ```sh
   git clone [https://github.com/seu-usuario/PTA-ciencia-de-dados-equipe-Julia.git](https://github.com/seu-usuario/PTA-ciencia-de-dados-equipe-Julia.git)
Entre na pasta do projeto:

Bash

cd PTA-ciencia-de-dados-equipe-Julia
Instale as dependências:

Bash

pip install pandas numpy fastapi uvicorn unidecode
Como Rodar a Análise
Para reproduzir os insights de consultoria e gerar a base consolidada para o Dashboard:

Certifique-se de que a pasta data/ contém os 4 arquivos CSV tratados (pedidos_tratados.csv, etc.).

Execute o script de análise:

Bash

python analise_negocio.py
O script irá gerar o arquivo base_consolidada_dashboard.csv na raiz do projeto e exibir os principais insights no terminal.

Insights Gerados
A análise revelou 3 gargalos críticos para a operação da O-Market:

Ineficiência Regional: O estado da região Norte apresenta taxa de atraso e cancelamento 3x superior à média nacional.

Erosão de Margem: Produtos de ticket baixo (< R$ 40) sofrem com frete que representa +50% do valor, matando a conversão.

Risco de Concentração: Dependência excessiva de vendedores em SP e alta taxa de cancelamento em parceiros específicos ("Vendedores Baleia").

Plano de Ação Proposto:

Implementação de estratégia de "Kitting" (Venda de Combos).

Auditoria logística nos estados críticos.

Expansão da malha de parceiros para o Norte/Nordeste.

Contato
CITi UFPE - contato@citi.org.br

Equipe de Dados O-Market (PTA 2025.2)