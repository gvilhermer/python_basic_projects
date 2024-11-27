import time
p = int(input('Primeiro valor:'))
s = int(input('Segundo valor:'))
op = 0
maior = p
while op != 5:
    op = int(input('''
    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NÚMEROS
    [5]SAIR DO PROGRAMA
    >>>Qual sua opção? '''))
    if op == 1:
        print('O resultado de {} + {} vale {}'.format(p, s, p+s))
    elif op == 2:
        print('O resultado de {} x {} vale {} '.format(p, s, p*s))
    elif op == 3:
        if s > p:
            maior = s
            print('O maior valor é {}'.format(maior))
    elif op == 4:
        p = int(input('Primeiro valor:'))
        s = int(input('Segundo valor:'))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    time.sleep(1.5)
print('Fim do programa.')