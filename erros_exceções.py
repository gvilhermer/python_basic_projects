try:
    a = int(input('Valor 1:'))
    b = int(input('Valor 2:'))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os valores que você digitou.')
except (ZeroDivisionError):
    print('Não é possível dividir um número por zero.')
except (KeyboardInterrupt):
    print('O usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'Ocorreu um problema: {erro.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre.')
