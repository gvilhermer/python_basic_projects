frase  = 'magrelin gostosin'
nova = frase.replace('magrelin', 'pintudin')
div = frase.split()
print(div[1][5])
print(frase .upper().find('MAGRELIN'))
print(nova)



#len(frase) > comprimento da string
#frase.count('g',0,11) > conta o n de vezes que a letra aparece dentro das posições
#frase.find('gos') > encontra o termo dentro dos parênteses
#frase.find('android') > se a palavra não existir será retornado o valor -1, já que a posição inicial é 0
#frase.replace('magrelin', 'android') > substitui a primeira palavra pela outra, ajustando o n de caracteres
#frase.upper() > deixa todas as letras maiúsculas
#frase.lower() > deixa todas as letras minúsculas
#frase.capitalize() > deixa todos os caracteres minúsculos, menos o primeiro
#frase.title() > deixa a primeira letra de cada palavra maiúscula
#frase.strip() > remove os espaços inúteis de uma frase, espaços no meio da frase são para quebrar palavras
#frase.split() > separa cada palavra colocando cada uma em um index diferente
#'-'.join(frase) > junta todas as palavras, separando-as com o caracter que estiver dentro das aspas