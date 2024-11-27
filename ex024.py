p = float(input('Qual o preço das compras? R$'))
f = int(input('''
Formas de pagamento
[1] à vista no dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais com juros
Qual a opção? '''))
if f == 1:
    print('Sua compra de R${:.2f} passará a custar R${:.2f} com o desconto de 10%.'.format(p, p-(p*(10/100))))
elif f == 2:
    print('Sua compra de R${:.2f} passará a custar R${:.2f} com o desconto de 5%'.format(p, p-(p*(5/100))))
elif f == 3:
    print('Sua compra de R${:.2f} terá 2 parcelas de R${:.2f}'.format(p, p/2))
elif f == 4:
    t = p+(p*20/100)
    a = int(input('Em quantas vezes quer parcelar?'))
    print('Sua compra de {:.2f} passará a custar {:.2f} com 20% de juros'.format(p, t), end='')
    print('e será divida em {}x de R${:.2f} no cartão.'.format(a, t/a))