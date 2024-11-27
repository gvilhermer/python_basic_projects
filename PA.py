pr = int(input('Primeiro termo:'))
rz = int(input('Razão da PA:'))
c = 1
primeiro = pr
#print(pr, end=' > ')
while c <= 10:
    print('{}'.format(primeiro), end=' > ')
    c += 1
    primeiro += rz
print('FIM')