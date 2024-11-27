n = c = s = 0
n = int(input('Digite um valor [999 para encerrar]:'))
while n != 999:
    c += 1
    s += n
    n = int(input('Digite um valor [999 para encerrar]:'))
print('Você digitou {} números e a soma deles equivale a {}'.format(c, s))