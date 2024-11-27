lanche = ('hamburguer', 'pizza', 'suco', 'pudim')
for comida in lanche:
    print(f'eu vou comer {comida}')

for c in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi por bosta')