# Gerando um número entre 0 e 5

import random

numero = int(input('Em qual número eu estou pensando entre 0 a 5?: '))
gerar = random.randint(0,5)

if numero == gerar:
  print('PARABÉNS! Você acertou, eu estava pensando neste número.')
else:
  print(f'TENTE NOVAMENTE! Eu não estava pensando no número {numero} e sim no {gerar}.')
