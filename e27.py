# primeiro nome e ultimo nome

nome = str(input('Digite seu nome completo: ')).strip().title()
lista = nome.split()
pri = lista[0]
#ult = lista.pop()
ult = lista[-1]

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {pri}.')
print(f'Seu último nome é {ult}.')