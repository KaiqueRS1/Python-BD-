quantidade_registro = int(
    input("Digite a quantidade de registros que deseja inserir: ")
)

resposta_corrompido = input("O arquivo está corrompido? s/n: ").strip().lower()

while resposta_corrompido != "s" and resposta_corrompido != "n":
    print("Resposta inválida.")

    resposta_corrompido = input(
        "Digite apenas s ou n: "
    ).strip().lower()

arquivo_corrompido = resposta_corrompido == "s"

resposta_csv = input("O arquivo é CSV? s/n: ").strip().lower()

while resposta_csv != "s" and resposta_csv != "n":
    print("Resposta inválida.")

    resposta_csv = input(
        "Digite apenas s ou n: "
    ).strip().lower()

arquivo_csv = resposta_csv == "s"

resposta_excel = input("O arquivo é Excel? s/n: ").strip().lower()

while resposta_excel != "s" and resposta_excel != "n":
    print("Resposta inválida.")

    resposta_excel = input(
        "Digite apenas s ou n: "
    ).strip().lower()

arquivo_excel = resposta_excel == "s"

if (
    quantidade_registro >= 100
    and not arquivo_corrompido
    and (arquivo_csv or arquivo_excel)
):
    print("Arquivo aprovado para processamento")
else:
    print("Arquivo bloqueado")

print("Validação finalizada")