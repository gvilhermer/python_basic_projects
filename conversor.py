n = int(input('Digite um número inteiro:'))
print('''Qual será a conversão?
[1] para binário
[2] para octal
[3] para hexadecimal''')
c = int(input('Sua opção:'))
if c == 1:
    print('O número {} convertido para binário é {}'.format(n, bin(n)))
elif c == 2:
    print('O número {} convertido para octal é {}'.format(n, oct(n)))
elif c == 3:
    print('O número {} convertido para hexadecimal é {}'.format(n, hex(n)))