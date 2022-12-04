# Utilizando Módulos / Bibliotécas
'''
import 123
from 123 import abc or a,c

math:
ceil - arredondar para cima
floor - arredondar para baixo
trunc - Elimina a ,> 
pow - potência
sqrt - rai quadrada
factorial - fatorial
'''
'''
#import math
from math import sqrt, floor

num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é {floor(raiz)}.')
'''
'''
# Blicliotéca random
import random

num = random.randint(1, 10)

print(num)
'''
#Bibliotéca emoji

import emoji
print(emoji.emojize('Olá, Mundo :earth_americas:', language='alias'))
