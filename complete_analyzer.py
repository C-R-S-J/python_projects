soma_idades = 0
mulheres = 0
velho_nome = ''
maioridadehomem = 0
for p in range (1,5):
    print(f'----{p}° PESSOA----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idades += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        velho_nome = nome
    if sexo in 'mM' and idade > maioridadehomem:
        maioridadehomem = idade
        velho_nome = nome
    if sexo in 'Ff' and idade < 20:
        mulheres += 1
media_idade = soma_idades / 4

print(f'A média da idade das pessoas cadastradas é {media_idade}')
print(f'O homem mais velho se chama {velho_nome} e tem {maioridadehomem}')
print(f'Há {mulheres} mulheres com menos de 20 anos')
