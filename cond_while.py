'''s = str(input('Informe seu sexo [M/F]:')).upper().strip()[0]
while s not in 'MF':
    s = str(input('Dados inválidos. Digite novamente:')).upper()
print('Dados registrados com sucesso!')'''


import random
c = random.randint(0, 10)
print('''
Sou seu computador...
acabei de pensar em um número entre 0 e 10.
Consegue adivinhar qual é?''')
acerto = False
p = 0
while not acerto:
    n = int(input('Qual seu palpite?'))
    p += 1
    if n == c:
        print('Acertou!')
        acerto = True   
    else:
        if n < c:
            print('Mais...Tente mais uma vez.')
        elif c < n:
            print('Menos...Tente mais uma vez.')
print('Você precisou de {} tentativas para acertar.'.format(p))