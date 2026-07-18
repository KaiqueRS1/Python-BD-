total_analisados = 0
total_aprovados = 0
total_bloqueados = 0

continuar = "s"

while continuar == "s":
    while True:
        try:
            quantidade_registros = int(
                input("Digite a quantidade de registros: ")
            )
            if quantidade_registros < 0:
                print(f"A quantidade ({quantidade_registros}) não pode ser negativa.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite apenas um número inteiro.")

    resposta_corrompido = input(
        "O arquivo está corrompido? s/n: "
    ).strip().lower()

    while resposta_corrompido != "s" and resposta_corrompido != "n":
        print("Resposta inválida.")

        resposta_corrompido = input(
            "Digite apenas s ou n: "
        ).strip().lower()

    arquivo_corrompido = resposta_corrompido == "s"


    resposta_csv = input(
        "O arquivo é CSV? s/n: "
    ).strip().lower()

    while resposta_csv != "s" and resposta_csv != "n":
        print("Resposta inválida.")

        resposta_csv = input(
            "Digite apenas s ou n: "
        ).strip().lower()

    arquivo_csv = resposta_csv == "s"


    resposta_excel = input(
        "O arquivo é Excel? s/n: "
    ).strip().lower()

    while resposta_excel != "s" and resposta_excel != "n":
        print("Resposta inválida.")

        resposta_excel = input(
            "Digite apenas s ou n: "
        ).strip().lower()

    arquivo_excel = resposta_excel == "s"


    total_analisados += 1

    if (
        quantidade_registros >= 100
        and not arquivo_corrompido
        and (arquivo_csv or arquivo_excel)
    ):
        print("Arquivo aprovado para processamento")
        total_aprovados += 1
    else:
        print("Arquivo bloqueado")
        total_bloqueados += 1


    continuar = input(
        "Deseja analisar outro arquivo? s/n: "
    ).strip().lower()

    while continuar != "s" and continuar != "n":
        print("Resposta inválida.")

        continuar = input(
            "Digite apenas s ou n: "
        ).strip().lower()


print("\n===== RELATÓRIO FINAL =====")
print(f"Total de arquivos analisados: {total_analisados}")
print(f"Arquivos aprovados: {total_aprovados}")
print(f"Arquivos bloqueados: {total_bloqueados}")
print("===========================")