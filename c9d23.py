# Unidade, Dezena, Centena, Milhar

num = int(input('Informe um número inteiro: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Sua Unidade é: {u}')
print(f'Sua Dezena é: {d}')
print(f'Sua Centena é: {c}')
print(f'Seu Milhar é: {m}')
