primeiro = int(input('Qual o primeiro termo: '))
razao = int(input('Qual a razão: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0 :
    total = total + mais
    while contador <= total:
        print(f'{termo} = ',end='')
        termo += razao
        contador += 1
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print(f'Fim de programa, {total} termos mostrados ao total')
