sal = float(input('Digite o seu salário para calcular seu aumento: '))
aum10 = float(sal * 0.1)
aum15 = float(sal * 0.15)

if sal > 1250:
  print(f'Seu salário com o aumentará R$ {aum10:.2f}, ficando R$ {(aum10 + sal):.2f}.')
if sal <= 1250:
  print(f'Seu salário com o aumentorá R$ {aum15:.2f}, ficando R$ {(aum15 + sal):.2f}.')