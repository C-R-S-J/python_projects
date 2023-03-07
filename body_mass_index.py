peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura**2)
if imc < 18.5:
    print(f'Você está com o imc em {imc:.2f}!')
    print(f'Você está abaixo do peso ideal!')
elif imc >= 18.5 and imc < 25:
    print(f'Você está com o imc em {imc:.2f}!')
    print('Você está com o pesoa ideal!')
elif imc >= 25 and imc < 30:
    print(f'Você está com o imc em {imc:.2f}!')
    print('Você está com sobrepeso!')
elif imc >= 30 and imc < 40:
    print(f'Você está com o imc em {imc:.2f}')
    print('Você está com obesidade!')
else:
    print(f'Você está com obesidade mórbida!')