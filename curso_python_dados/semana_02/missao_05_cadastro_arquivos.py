arquivos = []
continuar = "s"

while continuar == "s":
    
    nome_arquivo = input( "Digite o nome do arquivo: "
    ).strip()

    arquivos.append(nome_arquivo)

    continuar = input(
        "Deseja continuar? s/n: ").strip().lower()
    
print(f"Quantidade de arquivos: {len(arquivos)}")

for arquivo in arquivos:
    print(f"arquivo cadastrado: {arquivo}")