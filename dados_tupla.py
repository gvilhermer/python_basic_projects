num = (int(input('Digite um número:')),
       int(input('Digite um número:')),
       int(input('Digite um número:')),
       int(input('Digite um número:')))
print(f'Você digitou os valores: {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 está na posição {num.index(3)}')
else:
    print('O valor 3 não está em nenhuma posição.')