# Preço da passagem

dist = float(input('Digite quantos KM você deseja viajar para calcular o preço da passagem: '))
km1 = float(dist * 0.50)
km2 = float(dist * 0.45)

if dist <= 200:
  print(f'Sua viagem custará: R$ {km1}.')
else:
  print(f'Sua viagem custará R$ {km2}.')