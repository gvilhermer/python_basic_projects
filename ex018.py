a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c >b and b + c > a:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')