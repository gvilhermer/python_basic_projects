import random
#n1 = str(input('Primeiro aluno: '))
#n2 = str(input('Segundo aluno: '))
#n3 = str(input('Terceiro aluno: '))
#n4 = str(input('Quarto aluno: '))
#lista = [n1, n2, n3, n4]
#escolhido = random.choice(lista)
#print('O aluno escolhido foi: ', escolhido)


n1 = str(input('Primeiro: '))
n2 = str(input('Segundo: '))
n3 = str(input('Terceiro: '))
n4 = str(input('Quarto: '))
lista = [n1, n2, n3, n4]
ordem = random.shuffle(lista)
print('A ordem será: ')
print(lista)