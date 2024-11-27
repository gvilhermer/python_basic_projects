import math

a = float(input('Digite o valor de um ângulo: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))
print('SEN: {:.2f}, COS: {:.2f}, TG: {:.2f}'.format(sen, cos, tg))