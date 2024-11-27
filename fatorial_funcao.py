def fatorial(n, show=False):
    """
    Calcula o fatorial de um número.
    :param n: Número que será calculado.
    :param show: Parâmetro opcional para mostrar o cálculo feito.
    :return: Retorna o resultado do fatorial de n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c,  end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
#help(fatorial)
