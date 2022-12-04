# Escolher aleatóriamente um nome de aluno.

import random

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('digite o nome do quarto aluno: ')

aluno = random.choice([a1, a2, a3, a4])

print(f'O aluno escolhido foi: {aluno}')
