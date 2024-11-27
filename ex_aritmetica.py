n1 = int(input('Fala ai comédia: '))
n2 = int(input('Fala dnv largato: '))
a = n1+n2
s = n1-n2
m = n1*n2
d = n1/n2
dd = n1//n2
e = n1**n2
dr = n1%n2

print('Essas brincadeiras tudo são respectivamente: {}, {}, {}, {:.3f}'.format(a, s, m, d), end=' ')
print('As outras brincadeiras são: {}, {} e {}'.format(dd, e, dr))

# ordem de procedencia aritmética
# 1 ()
# 2 **
# 3 * / // %
# 4 + -
