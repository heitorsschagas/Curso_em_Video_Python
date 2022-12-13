# letra A
frase = str(input('Digite uma frase: ')).strip().lower()
qua = frase.count('a')
pri = frase.find('a')
ult = frase.rfind('a')

print(f'A letra A aparece {qua} vez(es) na frase.')
print(f'A primeira letra A apareceu na posição {pri+1}.')
print(f'A última letra A apareceu na posição {ult+1}.')