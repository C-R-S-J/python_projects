primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10-1) * razao
for c in range (primeiro,decimo,razao):
    print(c, end= ' = ')
print('ACABOU')