x = input('Digite algo: ')

print('O tipo primitivo de {} é'.format(x), type(x))
print('Só tem espaços?', x.isspace())
print('Só tem números?', x.isnumeric())
print('Só tem letras?', x.isalpha())
print('Tem letras e números (é alfanumérico)?', x.isalnum())
print('Está em maiúsculas?', x.isupper())
print('Está em minúsculas?', x.islower())
print('Está capitalizada?', x.istitle())      