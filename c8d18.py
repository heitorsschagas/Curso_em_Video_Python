# ângulo e mostre o seno, cosseno e tangente.

import math

ang = float(input('Digite o angulo º: ')) # Angulo
rad = math.radians(ang) # Radino
sen = math.sin(rad) # Seno
cos = math.cos(rad) # Cosseno
tan = math.tan(rad) # Tangente

print(f'Seu Seno é: {sen}')
print(f'Seu Cosseno é: {cos}')
print(f'Sua Tangente é: {tan}')
