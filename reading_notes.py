while True:
    nota = int(input('Digite uma nota entre 0 a 10: '))
    if nota < 0 or nota > 10:
        nota = int(input('Digite uma nota entre 0 a 10: '))
    elif nota > 0 or nota < 10:
        break
print('Nota lida com sucesso')