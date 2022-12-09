# Cidade
cidade = str(input('Digite o nome da sua cidade: ')).strip()
cidade = cidade.upper()
lista = cidade.split()
inicio = lista[0]

if inicio == 'SANTO':
  print('Sua cidade possui Santo no início.')
else:
  print('Sua cidade não possui Santo no início.')
