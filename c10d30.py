# PAR ou ÍMPAR

num = int(input('Digite um número inteiro para saber se ele é PAR ou ÍMPAR: '))
rest = num % 2

if rest == 0:
  print('Seu número é Par.')
else:
  print('Seu número é ÍMPAR.')