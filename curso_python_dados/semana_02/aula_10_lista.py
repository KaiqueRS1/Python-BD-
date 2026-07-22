arquivos = [
    "vendas.csv",
    "clientes.csv",
    "produtos.xlsx",
    "estoque.csv",
]

print(f"Quantidade de arquivos: {len(arquivos)}")
for arquivo in arquivos:
    print(f"processando: {arquivo}")