# Cadeia de caractéres
'''
# Analisando a String
len(), count(), find(), replace(), upper(), lower(), capitalize(), title(), r l strip(), join(), split().
'''
frase = 'Curso em Vídeo Python' # 21 caractéries
frase2 = '  Aprenda Python  '

print(len(frase))
print(frase.count('o',0,13))
print(frase.find('android'))
print(frase.replace('Python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase2.lstrip())
print(frase.split())
print('-'.join(frase))
'''
print("""asd
zxcdsafsfefef
jkleeeeeeeeeeeeeee
321511111111111111111111111111
789hgfdjrysdgsafdxgsdtrxghfcfg""")
'''
#print(frase.upper().count('O'))
