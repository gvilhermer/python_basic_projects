import datetime
ctps = dict()
ctps['nome'] = str(input('Nome:'))
ctps['nascimento'] = int(input('Ano de nascimento:'))
ctps['carteira'] = int(input('Carteira de trabalho(0 não tem):'))

if ctps['carteira'] != 0:
    ctps['contratação'] = int(input('Ano de contratação:'))
    ctps['salário'] = float(input('Salário:'))
    ctps['aposentadoria'] = (ctps['contratação'] + 35) - ctps['nascimento']

for k, v in ctps.items():
    print(f'{k} tem valor {v}')
