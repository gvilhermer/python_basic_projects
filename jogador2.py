time = []
jogador = dict()
gols = []
totalgols = 0
while True:
    jogador.clear()
    jogador['atleta'] = str(input('Nome do jogador:'))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador['atleta']} jogou?'))
    if jogador['partidas'] != 0:
        for c in range(0, jogador['partidas']):
            n = int(input(f'Quantos gols na partida {c+1}?'))
            gols.append(n)
            totalgols += n
    jogador['gols'] = gols.copy()
    jogador['total'] = totalgols
    time.append(jogador.copy())
    gols.clear()
    totalgols = 0
    while True:
        resp = str(input('Quer continuar? [ S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Responda apenas com sim ou não.')
    if resp == 'N':
        break
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<10}', end='')
    print()
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro. Não existe jogador com o índice {busca}.')
    else:
        print(f'Levantamento do jogador {time[busca]["atleta"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols.')