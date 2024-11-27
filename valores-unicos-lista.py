listinha = []
while True:
    v = int(input('Digite um valor:'))
    if v not in listinha:
        listinha.append(v)
        print('Valor adicinado!')
    else:
        print('O valor já está na lista...')
    resp = str(input('Quer continuar? [S/N]')).lower()
    if resp in 'n':
        break
    elif resp not in 'sn':
        print('Responde direito mlk')
listinha.sort()
print(f'Você digitou os valores: {listinha}')
