'''
# Operações aritméticas/Ordem 1234

(1) 
+ Adição (4)
- Subtração (4)
* Multiplicação (3)
/ Divisão (3)
** Potência (2)
// Divisão inteira (3)
% /resto da Divisão (3)
'''
'''
print(f'Sua Adição é: {n1 + n2}')
print(f'Sua Subtração é: {n1 - n2}')
print(f'Sua Multiplicação é: {n1 * n2}')
print(f'Sua Divisão é: {n1 / n2}')
print(f'Sua Potência é: {n1 ** n2}')
print(f'Sua Divisão Inteira é: {n1 // n2}')
print(f'Seu Resto da Divisão é: {n1 % n2}')
'''

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
a = n1 + n2
s = n1 - n2
m = n1 * n2 
d = n1 / n2
p = n1 ** n2 
di = n1 // n2
rd = n1 % n2

print(f'Sua Adição é: {a}')
print(f'Sua Subtração é: {s}')
print(f'Sua Multiplicação é: {m}')
print(f'Sua Divisão é: {d:.2f}')
print(f'Sua Potência é: {p}')
print(f'Sua Divisão Inteira é: {di:.2f}')
print(f'Seu Resto da Divisão é: {rd}')
