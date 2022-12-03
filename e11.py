# altura x largura

l = float(input('Largura da parede em metros: '))
a = float(input('Altura da parede em metros: '))
area = l * a
t = area / 2

print(f'Sua parede tem a dimensão de {l} x {a} e sua área é de {area}m².')
print(f'Para pintar essa parede, você precisará de {t:.3f} litros de tinta.')
