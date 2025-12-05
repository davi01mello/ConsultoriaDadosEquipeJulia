import pandas as pd
import os

# --- CONFIGURAÇÃO DE CAMINHOS (Antídoto para erro de pasta) ---
# Pega o diretório onde este script está
current_dir = os.path.dirname(os.path.abspath(__file__))
# Aponta para a pasta 'data' que deve estar ao lado do script
pasta_data = os.path.join(current_dir, "data")

print(f"📂 Procurando arquivos em: {pasta_data}")

def analisar_negocio():
    print("📊 INICIANDO ANÁLISE DE CONSULTORIA O-MARKET...")

    # 1. CARREGAR DADOS
    try:
        # Tenta listar o que tem na pasta para debug
        if os.path.exists(pasta_data):
            print(f"   Arquivos encontrados: {os.listdir(pasta_data)}")
        else:
            print(f"❌ A pasta '{pasta_data}' não existe!")
            return

        # Lendo os arquivos com caminho absoluto
        # Certifica-te de que os nomes dos arquivos na pasta 'data' são EXATAMENTE estes:
        # Lendo os arquivos com caminho absoluto (Nomes Corrigidos)
        df_itens = pd.read_csv(os.path.join(pasta_data, "itens_pedidos_tratados.csv"))
        df_pedidos = pd.read_csv(os.path.join(pasta_data, "pedidos_tratados.csv"))
        df_produtos = pd.read_csv(os.path.join(pasta_data, "produtos_tratados.csv"))
        df_vendedores = pd.read_csv(os.path.join(pasta_data, "vendedores_tratados.csv"))
        
        print(f"✅ Dados carregados: {len(df_itens)} itens vendidos.")

    except FileNotFoundError as e:
        print(f"❌ Erro específico ao abrir arquivo: {e}")
        return

    # 2. CRUZAMENTO (O Grande Merge)
    # Juntamos tudo numa tabela gigante usando os IDs
    print("🔄 Cruzando tabelas para visão 360º...")
    
    # Começa pelos itens (tabela fato) e junta com as outras (dimensões)
    df_completo = df_itens.merge(df_pedidos, on='order_id', how='inner')
    df_completo = df_completo.merge(df_produtos, on='product_id', how='inner')
    df_completo = df_completo.merge(df_vendedores, on='seller_id', how='inner')

    print(f"✅ Base consolidada gerada: {len(df_completo)} vendas com dados completos.")

    # 3. GERAR INSIGHTS (A parte de Consultoria)

    # Insight 1: Onde estão os atrasos? (Logística)
    if 'order_status' in df_completo.columns and 'order_delivered_customer_date' in df_completo.columns:
        # Filtra apenas pedidos entregues
        entregues = df_completo[df_completo['order_status'] == 'entregue'].copy()
        
        # Converte datas para garantir o cálculo
        entregues['data_entrega'] = pd.to_datetime(entregues['order_delivered_customer_date'], errors='coerce')
        entregues['data_estimada'] = pd.to_datetime(entregues['order_estimated_delivery_date'], errors='coerce')
        
        # Calcula dias de atraso (Real - Estimado)
        entregues['dias_atraso'] = (entregues['data_entrega'] - entregues['data_estimada']).dt.days
        
        # Cria flag: 1 se atrasou, 0 se chegou no prazo
        entregues['atrasou'] = entregues['dias_atraso'].apply(lambda x: 1 if x > 0 else 0)
        
        print("\n--- 🚚 INSIGHT 1: TOP 5 ESTADOS COM MAIS ATRASOS (Sellers) ---")
        # Calcula a média de atrasos por estado do vendedor
        ranking_atraso = entregues.groupby('seller_state')['atrasou'].mean().sort_values(ascending=False)
        print(ranking_atraso.head(5).apply(lambda x: f"{x*100:.1f}% dos pedidos atrasam"))

    # Insight 2: Custo de Frete (Gargalo de Vendas)
    if 'freight_value' in df_completo.columns and 'price' in df_completo.columns:
        # Garante que são números
        df_completo['freight_value'] = pd.to_numeric(df_completo['freight_value'], errors='coerce')
        df_completo['price'] = pd.to_numeric(df_completo['price'], errors='coerce')
        
        # Calcula quanto o frete representa do valor do produto
        df_completo['impacto_frete'] = df_completo['freight_value'] / df_completo['price']
        
        # Define gargalo: Frete custa mais de 50% do produto
        frete_caro = df_completo[df_completo['impacto_frete'] > 0.5] 
        
        print(f"\n--- 💸 INSIGHT 2: GARGALO LOGÍSTICO ---")
        print(f"Identificamos {len(frete_caro)} vendas onde o frete custa mais de METADE do valor do produto.")
        print("Categorias mais afetadas por frete caro:")
        print(frete_caro['product_category_name'].value_counts().head(3))

        # ... (código anterior) ...

    # INSIGHT 3: ANÁLISE DE "BAD REVENUE" (Faturamento Perdido)
    # Calcula o total vendido (Tudo que entrou como pedido)
    total_gmv = df_completo['price'].sum()
    
    # Calcula o que foi perdido (Cancelado ou Indisponível)
    perda_status = ['canceled', 'unavailable']
    df_perda = df_completo[df_completo['order_status'].isin(perda_status)]
    total_perdido = df_perda['price'].sum()
    
    # Porcentagem de perda
    porcentagem_perda = (total_perdido / total_gmv) * 100

    print(f"\n--- 📉 INSIGHT 3: EROSÃO DE RECEITA (CANCELAMENTOS) ---")
    print(f"Faturamento Total Processado: R$ {total_gmv:,.2f}")
    print(f"Receita Perdida (Cancelados): R$ {total_perdido:,.2f}")
    print(f"Impacto na Receita: {porcentagem_perda:.2f}%")
    print("Principais ofensores (Categorias com mais cancelamento):")
    print(df_perda['product_category_name'].value_counts().head(3))

    # 4. EXPORTAR PARA O DASHBOARD
    # Este é o arquivo que vais usar no Looker Studio / Power BI
    arquivo_saida = os.path.join(current_dir, "base_consolidada_dashboard.csv")
    df_completo.to_csv(arquivo_saida, index=False)
    print(f"\n💾 Arquivo final salvo em: {arquivo_saida}")
    print("👉 Usa este arquivo 'base_consolidada_dashboard.csv' para criar o teu Dashboard!")

if __name__ == "__main__":
    analisar_negocio()