# nome maiúsculo, minúsculo, quantidade de letras, primeiro nome e quantidade letras.

nome = str(input('Digite seu nome completo: ')).strip()
nupp = nome.upper()
nlow = nome.lower()
nspl = nome.split()
nrep = nome.replace(' ', '')

print(f'Seu nome em maiúsculas é {nupp}.')
print(f'Seu nome em minúsculas é {nlow}.')
print(f'Seu nome tem ao todo {len(nrep)} letras.')
print(f'Seu primeiro nome é {nspl[0]} e ele tem {len(nspl[0])} letras.')
