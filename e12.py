# Produto com desconto

p = float(input('Qual é o preço do produto? R$ '))
d = 5 / 100
pf = d * p

print(f'Produto que custava R$ {p:.2f}, na promoção com desconto de 5% irá custar R$ {p - pf:.2f}.')