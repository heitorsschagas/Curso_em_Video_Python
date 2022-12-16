# 3 retas, podem formar um triângulo

r1 = float(input('Digite o comprimento da Primeira reta: '))
r2 = float(input('Digite o comprimento da Segunda reta: '))
r3 = float(input('Digite o comprimento da Terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
  print('Suas 3 retas PODEM formar um triângulo.')
else:
  print('Suas 3 retas NÃO podem formar um triângulo.')
