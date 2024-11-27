rapaziada = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa['nome'] = str(input('Nome:'))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro. Digite apenas m ou f.')
    pessoa['idade'] = int(input('Idade:'))
    soma += pessoa['idade']
    rapaziada.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print(f'Ao todo temos {len(rapaziada)} pessoas cadastradas.')
media = soma / len(rapaziada)
print(f'A média de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end=' ')
for p in rapaziada:
    if p['sexo'] == 'F':
        print(f'{p['nome']}', end='')
print()
print('Lista das pessoas que estão com idade acima da média: ')
for p in rapaziada:
    if p['idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')
        print()