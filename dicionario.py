aluno = dict()
aluno['nome'] = str(input('Nome do aluno:'))
aluno['media'] = float(input('Média do aluno:'))

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 < aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print(f'O nome do aluno é {aluno['nome']}')
print(f'A média do aluno é {aluno['media']}')
print(f'A situação do aluno é {aluno['situação']}')