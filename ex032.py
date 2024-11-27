menor = 0
maior = 0
for c in range(1,6):
    p = float(input('Qual o peso da {}ª pessoa?'.format(c)))
    if c ==1:
        maior = c
        menor = c
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('O maior peso registrado foi de {}kg \nE o menor peso registrado foi de {}kg.'.format(maior, menor))