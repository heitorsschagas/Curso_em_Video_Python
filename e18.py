import math
'''
ang = float(input('Digite um anguloº: '))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)

print(f'Seu SENO é: {sen}')
print(f'Seu COSSENO é: {cos}')
print(f'E sua TANGENTE é: {tan}')
'''
ang = float(input('Digite um anguloº: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print(f'Seu SENO é: {sen:.2f}')
print(f'Seu COSSENO é: {cos:.2f}')
print(f'E sua TANGENTE é: {tan:.2f}')
