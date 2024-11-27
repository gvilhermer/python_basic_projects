#for c in range(2, 51, 2):
#    print(c, end=' ')


cont = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont += 1
print('A soma de todos os {} valores é {}'.format(cont, soma))