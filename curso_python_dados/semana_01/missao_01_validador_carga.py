quantidade_de_registro = int(input("Digite a quantidade de registros: "))

if quantidade_de_registro >= 100:
    print("arquivo aprovado para carga")
elif 1 <= quantidade_de_registro < 100:
    print("arquivo pequeno, precisa de revisão")
elif quantidade_de_registro == 0:
    print("arquivo vazio")
else:
    print("quantidade de registro inválido")


print("Validação concluída")