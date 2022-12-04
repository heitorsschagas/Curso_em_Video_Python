# Encontre a Hipotenusa

import math

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
cc = ((math.pow(co,2)) + (math.pow(ca,2)))
hip = math.sqrt(cc)

print(f'A Hipotenusa dos catetos {co} e {ca} é: {hip}.')