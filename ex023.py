kg = float(input('Qual seu peso (kg)?'))
h = float(input('Qual sua altura (m)?'))
imc = kg/h**2
if imc < 18.5:
    print('Seu IMC é de {:.2f} e você está abaixo do peso.'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é de {:.2f} e você está no peso ideal.'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é de {:.2f} e você está com sobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é de {:.2f} e você com obesidade.'.format(imc))
elif 40 <= imc:
    print('Seu IMC é de {:.2f} e você está com obesidade mórbida.'.format(imc))