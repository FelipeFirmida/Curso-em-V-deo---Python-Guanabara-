ano = int(input('Digite um ano: '))

if ((ano % 100) % 4 == 0):
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
