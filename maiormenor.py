resp = 'S'
soma = c = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número:'))
    c +=1
    soma += n
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
print('Você digitou {} números e a média entre eles é {}'.format(c, soma/c))
print('O maior número mostrado é {} e o menor é {}'.format(maior, menor))