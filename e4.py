# Testando a variável

da = input('Digite algo: ')

print('O tipo primitivo digitado é:', type(da))
print('Só tem espaços?', da.isspace())
print('É um número?', da.isnumeric())
print('É alfabético?', da.isalpha())
print('É alfanumérico', da.isalnum())
print('Está em maiúsculas?', da.isupper())
print('Está em minúsculas?', da.islower())
print('Está capitalizada?', da.istitle())
