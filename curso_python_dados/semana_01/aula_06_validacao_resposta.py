resposta = input("Deseja continuar? s/n: ").strip().lower()

while resposta != "s" and resposta != "n":
    print("Resposta inválida.")

    resposta = input(
        "Digite apenas s ou n: "
    ).strip().lower()

if resposta == "s":
    print("Processo continuará")
else:
    print("Processo encerrado")