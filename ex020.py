import datetime
a = int(input('Ano de nascimento:'))
h = datetime.date.today().year
if a + 18 == h:
    print('Você completa 18 anos e deve se alistar no ano de {}'.format(h))
elif a + 18 < h:
    print('Você tem {} anos, seu ano de alistamento foi em {}.'.format(h-a,a+18))
elif a + 18 > h:
    print('Você tem {} anos, deverá se alistar apenas em {}.'.format(h-a,a+18))