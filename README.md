# 🛍️ Projeto de Análise de Dados - Olist

Este projeto foi desenvolvido como trabalho final do curso de **Analista de Dados**, com o objetivo de aplicar na prática todas as etapas do processo de análise de dados: desde a coleta, tratamento e análise até a visualização dos insights.

---

## 📊 Descrição do Projeto

A análise foi realizada utilizando os dados públicos da empresa **Olist**, uma plataforma de e-commerce que conecta vendedores a grandes marketplaces no Brasil. O objetivo é gerar insights sobre as vendas, satisfação dos clientes, atrasos nas entregas e desempenho dos produtos.

---

## 🚀 Tecnologias Utilizadas

- Python 3.10
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Looker Studio (Google Data Studio)
- Jupyter Notebook / PyCharm
- Git e GitHub

---

## 🗂️ Estrutura do Projeto

📦 Projeto_Olist
├── dados/ # Dados tratados e prontos
├── imagens/ # Gráficos gerados pela análise
├── src/ # Arquivos de código Python
│ └── analise_olist.py # Código principal da análise
├── README.md # Descrição do projeto
├── requirements.txt # Bibliotecas necessárias


---

## 🔗 Base de Dados

Utilizamos os seguintes datasets da Olist:

- olist_customers_dataset.csv
- olist_geolocation_dataset.csv
- olist_order_items_dataset.csv
- olist_order_payments_dataset.csv
- olist_order_reviews_dataset.csv
- olist_orders_dataset.csv
- olist_products_dataset.csv
- olist_sellers_dataset.csv
- product_category_name_translation.csv

---

## 📈 Etapas do Projeto

### 1️⃣ Seleção dos Dados
- Fonte: Dados públicos da Olist.
- Selecionamos 9 tabelas, realizando o cruzamento entre elas.

### 2️⃣ Análise Exploratória
Foram realizadas análises como:
- Distribuição dos pedidos por categoria.
- Análise dos atrasos nas entregas.
- Avaliações dos clientes.
- Correlação entre tempo de entrega e nota de avaliação.
- Evolução de pedidos ao longo do tempo.

### 3️⃣ Tratamento dos Dados
- Padronização de colunas e datas.
- Tratamento de valores nulos e inconsistentes.
- Criação de variáveis novas como:
  - `tempo_entrega_real` (diferença entre entrega e compra).
  - `pedido_atrasado` (Sim/Não).

### 4️⃣ Visualização dos Dados
- Criação de gráficos interativos no Looker Studio.
- Dashboard completo e profissional.

---

## 📊 Visualizações Criadas

- 📅 Evolução dos pedidos por mês.
- 📦 Receita por categoria de produto.
- 🚚 Percentual de pedidos atrasados.
- ⭐ Avaliação média dos clientes vs. tempo de entrega.
- 📜 Tabela interativa com visão geral dos pedidos.

---

## 🖥️ Dashboard Interativo no Looker Studio

Acesse o dashboard clicando no link abaixo:

🔗 [**Dashboard no Looker Studio**](https://lookerstudio.google.com/reporting/27797ee0-59b6-46d8-916e-8d1f011751bb

) 

---

## 🏁 Como Executar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
