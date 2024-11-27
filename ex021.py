import datetime
i = int(input('Ano de nascimento do atleta?'))
a = datetime.date.today().year
if a - i <= 9:
    print('''O aleta tem {} anos.
Categoria: mirim.'''.format(a-i))
elif    a - i <= 14 and a - i >= 10:
    print('''O atleta tem {} anos.
Categoria: infantil.'''.format(a-i))
elif    a - i <= 19 and a - i >= 15:
    print('''O atleta tem {} anos.
Categoria: júnior.'''.format(a-i))
elif a - i <=25 and a - i >=20:
    print('''O atleta tem {} anos.
Categoria: sênior.'''.format(a-i))
elif a - i >25:
    print('''O atleta tem {} anos.
Categoria: master.'''.format(a-i))