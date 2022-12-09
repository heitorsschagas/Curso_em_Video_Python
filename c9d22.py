# Nome completo
'''
Mostrar o nome com as letras maiúscula
Mostrar o nome com as letras minusculas
Quantas letras tem o primeiro nome
'''
nome = str(input('Digite o seu nome completo: '))
separado = nome.split()

print(f'Convertendo tudo em maiúsculo fica: {nome.upper()}.')
print(f'Convertendo tudo em minisculo fica: {nome.lower()}.')
print(f'O primeiro nome contem {len(separado[0])} letras.')
