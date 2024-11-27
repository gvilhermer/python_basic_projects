ps = 0
cm = 0
cf = 0
while True:
    idade = int(input('Idade:'))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo [M/F]:')).upper().strip()[0]
    if idade >= 18:
        ps += 1
    if s in 'M':
        cm += 1
    if s in 'F' and idade < 20:
        cf += 1
    print('-' * 20)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]?')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Ao total foram cadastradas {ps} pessoas maiores de 18 anos.')
print(f'Foram cadastrados {cm} homens.')
print(f'Foram cadastradas {cf} mulheres com menos de 20 anos.')