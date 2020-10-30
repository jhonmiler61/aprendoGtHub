objetivo = int(input('Escoge un entero : '))
respuesta = 0

while respuesta**2 < objetivo:
    print(respuesta)
    respuesta += 1

if respuesta**2 == objetivo:
    print(f'La raiz cuadradad de {objetivo} es {respuesta}')
else:
    print('No tiene una raiz cuadrada exacta')

