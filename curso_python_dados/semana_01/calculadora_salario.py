Funcionario = input("Digite o nome do funcionário: ")
Horas_trabalhadas = float(input("Digite o as horas trabalhadas: "))
Valor_hora = float(input("Digite o valor da hora trabalhada:"))

salario = Horas_trabalhadas * Valor_hora 
print(f"o salário do funcionaro {Funcionario} é de R${salario:.2f}")