n = int(input('Diga um número:'))#
r = n % 2
cores = {
    'vermelho':'\033[31m',
    'azul':'\033[34m'
}
if r ==0:
    print('{}PAR'.format(cores['azul']))
else:
   print('{}ÍMPAR'.format(cores['vermelho']))


