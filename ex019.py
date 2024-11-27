valor = float(input('Qual o valor do imóvel? R$'))
sal = float(input('Qual seu salário? R$'))
ano = int(input('Quantos anos de financiamento?'))
pr = valor/(ano*12)         #prestação mensal
min = sal*30/100
cores = {
    'vermelho':'\033[31m',
    'verde':'\033[32m'
}
print('Para pagar R${} em {} anos, cada parcela será de R${:.2f}'.format(valor, ano, pr))
if pr <= min:
    print('\033[1;32mEmpréstimo concedido')
else:
    print('\033[1;31mEmpréstimo negado')