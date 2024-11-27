v = int(input('Qual a velocidade do carro?'))
if v <= 80:
    print('Boa viagem, dirija com cuidado!')
else:
    m = (v-80)*7
    print('Você ultrapassou o limite de velocidade e será multado em R${}'.format(m))