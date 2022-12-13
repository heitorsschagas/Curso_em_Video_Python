# nome completo, Silva = True

nome = str(input('Qual o seu nome completo?: ')).strip().upper()
lista = nome.split()
#silva = lista.count('SILVA') == 1
sil = 'SILVA' in nome

print(f'Seu nome tem Silva? = {sil}.')