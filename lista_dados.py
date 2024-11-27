valores = []
resp = ''
c = 0
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    c += 1
    resp = str(input('Quer continuar? [s/n]')).lower()
    if resp in 'n':
        break
valores.sort(reverse=True)
print(f'Você digitou {c} valores')
print(f'Os valores na forma decrescente são: {valores}')
if 5 in valores:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não faz parte da lista.')