# Cateto e Hipotenusa

from math import hypot
'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Compromento do cateto adjecente: '))
hip = math.sqrt((math.pow(co,2))+(math.pow(ca,2)))
print(f'A hipotenusa irá medir {hip}.')
'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Compromento do cateto adjecente: '))
hip = hypot(co, ca)
print(f'A hipotenusa irá medir {hip}.')
