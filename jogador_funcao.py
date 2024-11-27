def jogador(a='<desconhecido>', b=0):
    print(f'O jogador {a} fez {b} gols.')


nome = str(input('Nome do jogador:'))
gols = str(input('Número de gols:'))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    jogador(b=gols)
else:
    jogador(nome, gols)