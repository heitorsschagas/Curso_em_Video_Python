'''
#Real comprar dolar

c = float(input('Quanto dinheiro você tem na carteira? R$ '))
r = c * 1
d = r * 5.22

print(f'Com R$ {c:.2f} você pode comprar US$ {d:.2f}.')
'''

r = float(input('Digite um valor em R$ '))
d = float(input('Digote a cotação do dolar: US$ '))

cot = r / d

print(f'Você pode comprar US$ {cot:.2f}.')
