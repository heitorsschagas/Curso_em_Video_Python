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

.isnumeric() - se é numerico True/False
.isalpha() - se é letra True/False
.isalnym() - se é letra e/ou número True/False
.isupper() - se esta somente com letras maiúsculas True/False
'''

#n = bool(input('Digite um valor: '))
#print(f'O valor é: {n}')

n = input('Digite algo: ')
#print(n.isnumeric())
#print(n.isalpha())
#print(n.isalnum())
print(n.isupper())
