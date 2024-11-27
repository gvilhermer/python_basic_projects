def maior(*n):
    c = m = 0
    for v in n:
        print(v, end=' ')
        if c == 0:
            m = v
        else:
            if v > m:
                m = v
        c += 1
    print(f'\nO maior valor é {m}')


maior(2, 3, 5, 1)
maior(1, 9, 4, 7, 3)