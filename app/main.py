# ... imports ...

# --- ROTA 1: PEDIDOS ---
@app.get("/pedidos-tratados", description="Retorna base de pedidos tratada.")
async def get_pedidos_tratados(
    # AQUI ESTÁ A CORREÇÃO: Use o nome real do arquivo que está na pasta data
    arquivo: str = "pedidos_tratados.csv", 
    arquivo_itens: str = "itens_pedidos_tratados.csv",
    skip: int = Query(0, ge=0), 
    limit: int = Query(100, le=100)
):
    path_orders = f"data/{arquivo}"
    path_items = f"data/{arquivo_itens}"
    # ... resto da função ...

# --- ROTA 2: VENDEDORES ---
@app.get("/vendedores-tratados", description="Retorna base de vendedores tratada.")
async def get_vendedores_tratados(
    arquivo: str = "vendedores_tratados.csv", # Correção
    arquivo_itens: str = "itens_pedidos_tratados.csv", # Correção
    skip: int = Query(0, ge=0), 
    limit: int = Query(100, le=100)
):
    # ... resto da função ...

# --- ROTA 3: PRODUTOS ---
@app.get("/produtos-tratados", description="Retorna base de produtos tratada.")
async def get_produtos_tratados(
    arquivo: str = "produtos_tratados.csv", # Correção
    arquivo_itens: str = "itens_pedidos_tratados.csv", # Correção
    skip: int = Query(0, ge=0), 
    limit: int = Query(100, le=100)
):
    # ... resto da função ...

# --- ROTA 4: ITENS PEDIDOS ---
@app.get("/itens-tratados", description="Retorna base de itens tratada.")
def get_itens_tratados(
    arquivo_itens: str = "itens_pedidos_tratados.csv", # Correção
    arquivo_pedidos: str = "pedidos_tratados.csv",     # Correção
    arquivo_produtos: str = "produtos_tratados.csv",   # Correção
    arquivo_vendedores: str = "vendedores_tratados.csv", # Correção
    skip: int = Query(0, ge=0),
    limit: int = Query(100, le=100)
):
    # ... resto da função ...python analise_negocio.py
    