palavras = ('aprender', 'fisiculturismo', 'supino',
'malvado', 'largato', 'mulherada', 'selva')
for l in palavras:
    print(f'\nNa palavra {l.upper()} temos ', end=' ')
    for letra in l:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')