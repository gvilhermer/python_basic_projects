pares = []
impares = []
todos = []
while True:
    n = int(input('Digite um número: '))
    todos.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    resp = str(input('Quer continuar? [s/n]')).lower()
    if resp in 'n':
        break
print(f'A lista de todos os números é: {todos}')
print(f'A lista dos números pares é: {pares}')
print(f'A lista dos números ímpares é: {impares}')