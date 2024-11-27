jogador = dict()
gols = []
totalgols = 0
jogador['atleta'] = str(input('Nome do jogador:'))
jogador['partidas'] = int(input(f'Quantas partidas {jogador['atleta']} jogou?'))
if jogador['partidas'] != 0:
    for c in range(0, jogador['partidas']):
        n = int(input(f'Quantos gols na partida {c+1}?'))
        gols.append(n)
        totalgols += n
jogador['gols'] = gols.copy()
jogador['total'] = totalgols
print(jogador)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print(f'O jogador {jogador['atleta']} jogou {jogador['partidas']} partidas')
for g in range(0, jogador['partidas']):
    print(f'Na partida {g+1} marcou {gols[g]} gols.')
print(f'Tendo um total de {jogador['total']} gols')