import time
import random
itens = ('Pedra', 'Papel', 'Tesoura')
pc = random.randint(0,2)
a = int(input('''
Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual sua jogada?'''))
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!')
time.sleep(0.5)
print('O pc escolheu {}!'.format(itens[pc]))
print('O jogador escolheu {}!'.format(itens[a]))
if pc == 0 and a == 1 or pc == 1 and a == 2 or pc == 2 and a == 0:
    print('O jogador venceu!')
elif  a == 0 and pc == 1 or a == 1 and pc == 2 or a == 2 and pc == 0:
    print('O computador venceu!')
elif a == pc:
    print('Empate!')