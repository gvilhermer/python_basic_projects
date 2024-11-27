somai = 0
maiori = 0
velho = ''
muie = 0
for c in range(1,5):
    print('{}ª PESSOA'.format(c))
    n = str(input('Nome:')).strip()
    i = int(input('Idade:'))
    s = str(input('Sexo [M/F]:')).strip().upper()
    if s in 'Ff' and i <20:
        muie = muie + 1
    if c ==1 and s in 'Mm':
        maori = i
        velho = n
    if s in 'Mm' and i > maiori:
        maiori = i
        velho = n
    somai += i
md = somai/4
print('A média de idade do grupo é de {} anos.'.format(md))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiori, velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(muie))