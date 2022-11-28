#Largura e Altura de uma parade, quanto de tinta irá utilizar,1l=2m²?

x = float(input('Digite a Largura da parede em Metros: '))
y = float(input('Digite a Altura da parede em Metros: '))
a = x * y
t = a / 2

print(f'Sua parede possui: {a}m², sendo necessário: {t} Litros de tinta para pintar.')