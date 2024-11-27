primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
termo = primeiro
c = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{}'.format(termo), end=' > ')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar?'))
print('Você finalizou a P.A com {} termos mostrados.'.format(c))