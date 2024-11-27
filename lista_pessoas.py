princ = []
temp = []
maior = menor = 0
while True:
    temp.append(str(input('Nome:')))
    temp.append(float(input('Peso:')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if maior < temp[1]:
            maior = temp[1]
        if menor > temp[1]:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [s/n]')).lower()
    if resp in 'n':
        break
print(f'Você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {maior}, peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O menor peso foi de {menor}, peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}')