def leiaInt(msg):
    while True:
        try:
            v = int(input(msg))
        except (ValueError, TypeError):
            print(f'O valor digitado não é considerado um número inteiro.')
            continue
        except (KeyboardInterrupt):
            print('O usuário não informou o número.')
            return 0
        else:
            return v


def leiaFloat(msg):
    while True:
        try:
            v2 = float(input(msg))
        except (ValueError, TypeError):
            print('O valor digitado não é considerado um número real.')
            continue
        except (KeyboardInterrupt):
            print('O usuário não informou o número.')
            return 0
        else:
            return v2


num = leiaInt('Digite um número inteiro:')
num2 = leiaFloat('Digite um número real:')
print(f'O número inteiro é {num} e o número real é {num2}')
