from random import randint
cpf = []
multiplicador = 10
multiplicados = []
soma = 0
'''sorteia 9 numeros aleatórios para compor a primeira parte do CPF 
'''
for i in range(0, 9):
    cpf.append(randint(0, 9))
    multiplicados.append(cpf[i] * multiplicador)
    multiplicador -= 1
    soma += cpf[i]
'''calcula qual sera o 10° número a ser adicinado no CPF
'''
if soma % 11 < 2:
    cpf.append(0)
else:
    cpf.append(11 - (soma % 11))

multiplicador = 11
multiplicados.clear()
soma = 0
for i in range(0, 10):
    multiplicados.append(cpf[i] * multiplicador)
    multiplicador -= 1
    soma += cpf[i]

if soma % 11 < 2:
    cpf.append(0)
else:
    cpf.append(11 - (soma % 11))

print(f'O número do CPF é: {cpf}')