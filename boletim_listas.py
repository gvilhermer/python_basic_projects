ficha = list()
while True:
    aluno = str(input('Nome do aluno:'))
    n1 = float(input('Primeira nota:'))
    n2 = float(input('Segunda nota:'))
    media = (n1 +n2) / 2
    ficha.append([aluno, [n1, n2], media])
    resp = str(input('Quer continuar? [s/n]')).lower()
    if resp in 'n':
        break
for i, a in enumerate(ficha):
    print(f'{i} {a[0]} {a[2]}')
while True:
    opc = int(input('Quer mostrar as notas de qual aluno? [999 interrompe]'))
    if opc == 999:
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')