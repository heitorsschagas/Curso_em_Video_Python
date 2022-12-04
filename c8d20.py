# Escolher a ordem sortiada dos alunos      shuffle

import random

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('digite o nome do quarto aluno: ')

a1234 = [a1, a2, a3, a4]

aluno = random.shuffle(a1234)

print(f'A seguencia será: {a1234}')