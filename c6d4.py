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
.isalnum() - se é letra e/ou número True/False
.isupper() - se esta somente com letras maiúsculas True/False
'''

a = input('Digite uma letra e/ou número: ')
'''
# Modo 1
print('É numérico:', a.isnumeric(),'É letra', a.isalpha(), 'É alfanumérico', a.isalnum())
'''
# Modo 2
if a.isnumeric():
  print(f'{a} é numérico',type(a))
elif a.isalpha():
  print(f'{a} é alfabético',type(a))
elif a.isalnum():
  print(f'{a} é alfanumérico',type(a))
else:
  print(f'{a} não é valido',type(a))

'''
# Modo 3
print('Tipo primitivo:',type(a))
print('Alfabético:', a.isalpha())
print('Numérico:', a.isnumeric())
print('Alfanumérico:', a.isalnum())
'''