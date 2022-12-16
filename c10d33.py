# Qual é menor e maior

n1 = float(input('Digite o Primeiro número: '))
n2 = float(input('Digite o Segundo número: '))
n3 = float(input('Digite o Terceiro número: '))

if n1 == n2 or n1 == n3 or n2 == n3:
  print('Existem números repetidos, por favor, colocar apenas números diferentes.')
if n1 > n2 and n1 > n3:
  print(f'O número {n1} é o MAIOR.')
if n1 < n2 and n1 < n3:
  print(f'O número {n1} é o MENOR.')
if n2 > n1 and n2 > n3:
  print(f'O número {n2} é o MAIOR.')
if n2 < n1 and n2 < n3:
  print(f'O número {n2} é o MENOR.')
if n3 > n2 and n3 > n1:
  print(f'O número {n3} é o MAIOR.')
if n3 < n2 and n3 < n1:
  
  print(f'O número {n3} é o Menor.')