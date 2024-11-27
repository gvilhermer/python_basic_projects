import random
from time import sleep
m = random.randint(0,5)
n = int(input('Tente adivinhar o número entre 0 e 5:'))
print('Aguarde...')
sleep(2)
if n == m:
    print('acertou')
else:
    print('errou, largato')