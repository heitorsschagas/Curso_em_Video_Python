# ano BISSEXTO

ano = int(input('Digite um ano para saber se ele é BISSEXTO: '))
bis = (ano % 4 == 0 and ano % 100!=0) or (ano % 400 == 0)

if bis == 0:
  print('O ano não é Bissexto.')
else:
  print('O ano é Bissexto.')