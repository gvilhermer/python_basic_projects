from random import randint
while True:
    v = int(input('Digite um valor:'))
    comp = randint(0 ,10)
    total = v + comp
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('PAR ou ÍMPAR [P/I]?')).upper().strip()[0]
    print(f'Você jogou {v} e o computador jogou {comp}')
    if tipo == 'P':
        if total % 2 == 0:
            print('O jogador venceu!')
        elif total % 2 == 1:
            print('O computador venceu!')
            break
    elif tipo == 'I':
        if total % 2 == 0:
            print('O computador venceu!')
            break
        elif total % 2 == 1:
            print('O jogador venceu!')