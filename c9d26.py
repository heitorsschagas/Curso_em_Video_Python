# Quantas letras 'A' aparecem na frase e em que posição aparece na primeira e última vez.

frase = input('Digite uma frase: ')
a = frase.count('a')
p = frase.find('a')
u = frase.rfind('a')

print(f'A letra *A* aparece {a} vez(es) nesta frase.')
print(f'A letra *A* aparece primeiramente na posição {p}.')
print(f'A letra *A* aparece por último na posição {u}.')