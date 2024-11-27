f = str(input('Digite uma frase:')).strip().upper()
p = f.split()
j = ''.join(p)
inverso = ''
for letra in range(len(j)-1, -1, -1):
    inverso += j[letra]
if j == inverso:
    print('Temos um palíndromo')
else:
    print('A frase não é um palíndromo.')