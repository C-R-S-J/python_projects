nota_um = float(input('Digite a primeira nota do aluno: '))
nota_dois = float(input('Digite a segunda nota do aluno: '))
nota_final = (nota_um + nota_dois) / 2
if nota_final >= 6.0:
    print(f'A média final foi {nota_final}, portanto o aluno está APROVADO!')
elif nota_final < 6.0:
    print(f'A média final foi {nota_final}, portanot o aluno está de RECUPERAÇÃO!')