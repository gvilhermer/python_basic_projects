def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            ok = True
            valor = int(n)
        else:
            print('Digite um número inteiro válido.')
        if ok:
            return valor


n = leiaInt('Digite um número:')
print(f'Você digitou o número {n}.')