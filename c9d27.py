# Mostrar o primeiro e ultimo nome

nome = input('Digite um nome completo: ')
sep = nome.split()
pri = sep[0]
ult = sep.pop()

print(f'Seu primeiro nome é: {pri}.')
print(f'Seu último nome é: {ult}.')