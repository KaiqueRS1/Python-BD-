
continuar = "s"
total_arquivos = 0 

while continuar == "s":
    nome_arquivo = input("Digite o nome do arquivo: ")
    print(f"Arquivo {nome_arquivo} analisado")
    total_arquivos += 1

    continuar = input("Deseja analisar outro arquivo? (s/n): ").strip().lower()

    while continuar != "s" and continuar != "n":
        print("Resposta inválida.")

        continuar = input("Digite apenas s ou n: ").strip().lower()
print(f"Total de arquivos analisados: {total_arquivos}")
print ("Processo encerrado")