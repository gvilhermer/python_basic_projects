totalc = c = maisb = 0
nomeb = ' '
while True:
    nome = str(input('Nome do produto:'))
    preco = float(input('Preço: R$'))
    totalc += preco
    if preco > 1000:
        c += 1
    if c == 1:
        maisb = preco
        nomeb = nome
    if preco < maisb:
        maisb = preco
        nomeb = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]?')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O total da compra foi de R${totalc:.2f}.')
print(f'Temos {c} produtos acima de R$1000.')
print(f'O produto mais barato foi {nomeb} que custa R${maisb}.')