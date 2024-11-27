n = int(input('Digite um número:'))
t = 0
for c in range(1, n+1):
    if n % c ==0:
        print('\033[34m', end=' ')
        t +=1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print('\n\033[mO número {} foi divido {} vezes'.format(n, t))
if t ==2:
    print('É um número primo.')
else:
    print('Não é um número primo.')
