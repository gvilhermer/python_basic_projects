import random
print('Tente adivinhar o número de 0 a 10 que o computador pensou.')
c = random.randint(0,10)
p = 0
n = ''
while n != c:
    n = int(input('Digite um número:'))
    p += 1
    if n == c:
        print('Você acertou!')
    else:
        if n < c:
            print('Mais...Tente outra vez.')
        elif n > c:
            print('Menos...Tente outra vez.')
print('Você precisou de {} tentativas para acertar.'.format(p))