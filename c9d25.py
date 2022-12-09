# Tem 'CHAGAS' no nome?

nome = input('Digite seu nome completo: ')
nome = nome.upper()
verificar = 'CHAGAS' in nome


if verificar == True:
  print('Seu nome possui CHAGAS.')
else:
  print('Seu no não possui CHAGAS.')
