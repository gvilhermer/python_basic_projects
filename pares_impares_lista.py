numeros = [[], []]
valor = 0
for n in range(1, 8):
    valor = int(input(f'Digite o {n}° valor:'))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares são {numeros[0]}, e os valores ímpares são {numeros[1]}.')