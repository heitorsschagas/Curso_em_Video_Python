'''#Tipos Primitivos e Saída de dados
int - número inteiros                 : 123
float - números reais/flutuantes      : 1.5   0.025    -1.5   2.0
bool - valores lógicos ou booleanos   : True False
str - valores caracteris ou string    : 'escrita 123.123' ''

format - podendo usar:
(f'test{t}')
('test{}'.format(t))
****
n1 = int(1)
n2 = int(2)
soma = n1 + n2

print(f'A soma vale: {soma}') 
or
print(('A soma vale: {}').format(soma))
'''

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print(f'A soma entre {n1} e {n2} vale: {s}')
