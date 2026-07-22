senha = input("senha correta é ")
resposta_senha = input("coloque uma senha: ")

while resposta_senha != senha:
    print(f"a {resposta_senha} está incorreta tente novamente ")
    resposta_senha = input ("digite novamente: ") 

print("fim")
