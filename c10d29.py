# lendo a velocidade km

vel = int(input('Digite a sua velocidade: '))
mul = float((vel - 80)*7)

if vel <= 80:
  print('Você não ultrapassou o limite de 80km/h e não levou multa.')
else:
  print(f'Você ultrapassou o limite máximo de 80km/h e levou uma multa de R$ {mul}.')
  