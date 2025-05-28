# Importando as bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Configurações
sns.set(style="whitegrid")

# Leitura dos dados
clientes = pd.read_csv('dados/olist_customers_dataset.csv')
geolocalizacao = pd.read_csv('dados/olist_geolocation_dataset.csv')
itens_pedidos = pd.read_csv('dados/olist_order_items_dataset.csv')
pagamentos = pd.read_csv('dados/olist_order_payments_dataset.csv')
reviews = pd.read_csv('dados/olist_order_reviews_dataset.csv')
pedidos = pd.read_csv('dados/olist_orders_dataset.csv')
produtos = pd.read_csv('dados/olist_products_dataset.csv')
vendedores = pd.read_csv('dados/olist_sellers_dataset.csv')
categorias = pd.read_csv('dados/product_category_name_translation.csv')

# Merge dos dados
df = pedidos.merge(itens_pedidos, on='order_id') \
            .merge(pagamentos, on='order_id') \
            .merge(reviews, on='order_id') \
            .merge(produtos, on='product_id') \
            .merge(categorias, on='product_category_name', how='left')

# Tratamento de datas
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])

# Limpeza de dados
df = df.dropna(subset=['order_delivered_customer_date', 'order_estimated_delivery_date'])

# Criação de novas colunas
df['tempo_entrega_real'] = (df['order_delivered_customer_date'] - df['order_purchase_timestamp']).dt.days
df['pedido_atrasado'] = df['order_delivered_customer_date'] > df['order_estimated_delivery_date']

# Salvar base tratada
df.to_csv('dados/dados_tratados.csv', index=False)

# Análises Exploratórias e Visualizações
# 1. Distribuição do Tempo de Entrega
plt.figure(figsize=(10,6))
sns.histplot(df['tempo_entrega_real'], bins=30, kde=True)
plt.title('Distribuição do Tempo de Entrega')
plt.xlabel('Dias')
plt.ylabel('Quantidade de Pedidos')
plt.savefig('imagens/distribuicao_tempo_entrega.png')
plt.close()

# 2. Percentual de Pedidos Atrasados
plt.figure(figsize=(6,5))
sns.countplot(x='pedido_atrasado', data=df, palette='Set2')
plt.title('Pedidos Atrasados')
plt.xlabel('Atrasado')
plt.ylabel('Quantidade')
plt.savefig('imagens/pedidos_atrasados.png')
plt.close()

# 3. Avaliação por Atraso
plt.figure(figsize=(8,6))
sns.boxplot(x='pedido_atrasado', y='review_score', data=df, palette='Set3')
plt.title('Review Score x Atraso')
plt.xlabel('Pedido Atrasado')
plt.ylabel('Review Score')
plt.savefig('imagens/review_score_atraso.png')
plt.close()

# 4. Receita por Categoria
receita_categoria = df.groupby('product_category_name_english')['price'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
receita_categoria.plot(kind='bar', color='green')
plt.title('Top 10 Categorias com Maior Receita')
plt.xlabel('Categoria')
plt.ylabel('Receita Total')
plt.xticks(rotation=45)
plt.savefig('imagens/receita_categoria.png')
plt.close()

# 5. Evolução de Pedidos ao Longo do Tempo
pedidos_tempo = df.groupby(df['order_purchase_timestamp'].dt.to_period('M')).order_id.nunique()
plt.figure(figsize=(12,6))
pedidos_tempo.plot(kind='line', marker='o', color='purple')
plt.title('Evolução dos Pedidos')
plt.xlabel('Data')
plt.ylabel('Quantidade de Pedidos')
plt.grid()
plt.savefig('imagens/evolucao_pedidos.png')
plt.close()

print("Análise concluída com sucesso. As imagens estão salvas na pasta 'imagens' e a base tratada na pasta 'dados'.")
