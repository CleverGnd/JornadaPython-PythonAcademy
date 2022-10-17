idade = int(input('Digite a sua idade: '))
sexo = input('Digite a seu sexo (M para Masculino e F para Feminino): ')

if sexo.upper() == 'M': # Upper transforma para maiúsculo
    # Código para sexo masculino
    if idade >= 65:
        print('Parabéns! Sua aposentadoria será concedida!')
    else:
        print(f'Sua vez ainda não chegou! Aguarde mais {65 - idade} anos.')

elif sexo.upper() == 'F':
    # Código para sexo feminino
    if idade >= 60:
        print('Parabéns! Sua aposentadoria será concedida!')
    else:
        print(f'Sua vez ainda não chegou! Aguarde mais {60 - idade} anos.')

else:
    print('Opção inválida!')
