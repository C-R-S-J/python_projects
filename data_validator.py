
sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Opção inválida, digite novamente: ')).upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso!')
