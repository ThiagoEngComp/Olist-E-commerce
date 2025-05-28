import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Criar pastas para salvar outputs
os.makedirs('imagens', exist_ok=True)
os.makedirs('dados', exist_ok=True)

# Carregar os dados
customers = pd.read_csv('/mnt/data/olist_customers_dataset.csv')
geolocation = pd.read_csv('/mnt/data/olist_geolocation_dataset.csv')
order_items = pd.read_csv('/mnt/data/olist_order_items_dataset.csv')
order_payments = pd.read_csv('/mnt/data/olist_order_payments_dataset.csv')
order_reviews = pd.read_csv('/mnt/data/olist_order_reviews_dataset.csv')
orders = pd.read_csv('/mnt/data/olist_orders_dataset.csv')
products = pd.read_csv('/mnt/data/olist_products_dataset.csv')
sellers = pd.read_csv('/mnt/data/olist_sellers_dataset.csv')
product_category = pd.read_csv('/mnt/data/product_category_name_translation.csv')

# Mesclar tabelas principais
df = orders.merge(order_items, on='order_id')\
           .merge(order_payments, on='order_id')\
           .merge(order_reviews, on='order_id')\
           .merge(customers, on='customer_id')\
           .merge(products, on='product_id')\
           .merge(sellers, on='seller_id')\
           .merge(product_category, on='product_category_name', how='left')

# Tratamento de datas
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])

# Criar coluna se o pedido foi atrasado
df['pedido_atrasado'] = df['order_delivered_customer_date'] > df['order_estimated_delivery_date']

# Criar coluna de tempo de entrega
df['tempo_entrega'] = (df['order_delivered_customer_date'] - df['order_purchase_timestamp']).dt.days

# Análise Exploratória

# 1. Distribuição das avaliações
plt.figure(figsize=(8,5))
sns.countplot(x='review_score', data=df, palette='Set2')
plt.title('Distribuição das Avaliações')
plt.savefig('imagens/distribuicao_avaliacoes.png')
plt.close()

# 2. Análise de pedidos atrasados
plt.figure(figsize=(8,5))
sns.countplot(x='pedido_atrasado', data=df, palette='Set2')
plt.title('Pedidos Atrasados')
plt.savefig('imagens/pedidos_atrasados.png')
plt.close()

# 3. Boxplot tempo de entrega por atraso
plt.figure(figsize=(8,5))
sns.boxplot(x='pedido_atrasado', y='tempo_entrega', data=df, palette='Set3')
plt.title('Tempo de Entrega x Pedido Atrasado')
plt.savefig('imagens/tempo_entrega_atraso.png')
plt.close()

# 4. Quantidade de itens por pedido
plt.figure(figsize=(8,5))
sns.histplot(df['order_item_id'], kde=True, bins=10, color='orange')
plt.title('Distribuição da Quantidade de Itens por Pedido')
plt.savefig('imagens/quantidade_itens.png')
plt.close()

# 5. Meios de pagamento mais utilizados
plt.figure(figsize=(8,5))
sns.countplot(x='payment_type', data=df, palette='Set1', order=df['payment_type'].value_counts().index)
plt.title('Distribuição dos Meios de Pagamento')
plt.savefig('imagens/meios_pagamento.png')
plt.close()

# Salvar dataset tratado
df.to_csv('dados/dataset_tratado.csv', index=False)

