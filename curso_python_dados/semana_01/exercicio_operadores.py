total_registros = int(input("Digite a quantidade total de registros: "))
registros_por_arquivo = int(input("Digite quantos registros cabem em cada arquivo: "))
Arquivos_completos = total_registros // registros_por_arquivo
Registros_restantes = total_registros % registros_por_arquivo 

print(f"Arquivos completos: {Arquivos_completos}")
print(f"Registros restantes: {Registros_restantes}")