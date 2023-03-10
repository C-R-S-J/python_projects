from datetime import date
atual = date.today().year
contador = 0
jovens = 0
adultos = 0
for c in range(1, 8):
    nasc = int(input(f'Digite o ano que a {c}° pessoa nasceu: '))
    contador += 1
    idade = atual - nasc
    if idade < 18:
        jovens += 1
    else:
        adultos += 1
print(f'Há {jovens} pessoas menor de idade e {adultos} pessoas maior de idade')