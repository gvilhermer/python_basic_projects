import datetime
m = 0
v = 0
for c in range(1 ,8):
     data = int((input('Em que ano a {}ª nasceu?'.format(c))))
     if datetime.date.today().year - data < 18:
            m +=1
     else:
            v +=1
print('Ao todo tivemos {} pessoas menores de idade \nE {} pessoas maiores de idade.'.format(m, v))