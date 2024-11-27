ordem = []
for c in range(0,5):
    t = int(input('Digite um número:'))
    if c == 0 or t > ordem[-1]:
        ordem.append(t)
    else:
        pos = 0
        while pos < len(ordem):
            if t <= ordem[pos]:
                ordem.insert(pos, t)
                break
            pos += 1
print(f'Os valores digitados em ordem foram: {ordem}')
