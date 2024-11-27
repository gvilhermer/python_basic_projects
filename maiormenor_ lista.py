numeros = list()
ma = 0
me = 0
for cont in range(0,5):
    numeros.append(int(input(f'Digite um valor para a posição {cont}:')))
    if cont == 0:
        ma = me = numeros[cont]
    if ma < numeros[cont]:
        ma = numeros[cont]
    if me > numeros[cont]:
        me = numeros[cont]
print(f'Os valores digitados foram: {numeros}')
print(f'O maior valor digitado foi {ma}', end=' ')
for i, v in enumerate(numeros):
    if v == ma:
       print(f'e está na posição {i}')
print(f'O menor valor digitado foi {me}', end=' ')
for i, v in enumerate(numeros):
    if v == me:
        print(f'e está na posição {i}')
