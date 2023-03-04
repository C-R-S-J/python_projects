a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b >= c and b + c >= a and a + c >= b:
    print('As medidas formam um triânuglo!')
else:
    print('As medidas não formam um triânuglo')