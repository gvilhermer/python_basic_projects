a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b<a  and b<c:
    menor = b
if  c<b and c<a:
    menor = c
print('O menor valor é {}'.format(menor))

maior = b
if a>b and a>c:
    maior = a
if c>b and c>a:
    maior = c
print('O maior valor é {}'.format(maior))
