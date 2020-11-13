mi_tupla = ()
type(mi_tupla)
print(type(mi_tupla))

otra_tupla = (1, 'dos', True)
print(otra_tupla[0])

tupla = (1,)
print(type(tupla))

mi_otra_tupla = (1,2,3,4)
mi_tuplita = (1,2,3,4)

mi_tuplita += mi_otra_tupla
print(mi_tuplita)

w,x,y,z = mi_otra_tupla
print(w)
print(x)
print(y)
print(z)

def coordenadas():
    return (5,4)

coordenada = coordenadas()
a,b = coordenada
print(a)
print(b)