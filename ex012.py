#f = str(input('Digite uma frase:')).lower().strip()
#print('A letra A aparece {} vezes'.format(f.count('a')))
#print('A primeira vez que a letra aparece é na posição {}'.format(f.find('a')+1))
#print('A última vez que a letra aparece é na posição {}'.format(f.rfind('a')+1))


n = str(input('Digite seu nome completo:')).strip().split()
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))
