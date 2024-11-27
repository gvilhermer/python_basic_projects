'''num = [4, 9, 6, 1]
num[2] = 3
num.append(7)
num.insert(1, 5)
num.insert(2, 2)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''

valores = list()
'''valores.append(5)
valores.append(9)
valores.append(1)'''
for co in range(0, 5):
    valores.append(int(input('Digite um valor:')))
for c, v in enumerate(valores):
    print(f'Encontrei o valor {v} na posição {c}')