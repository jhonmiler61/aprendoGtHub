mi_lista = [1,2,3]
print(mi_lista[1])
print(mi_lista[1:])

mi_lista.append(4)
print(mi_lista)
mi_lista[0]='a'
print(mi_lista)
print(mi_lista.pop())
print(mi_lista)

for element in mi_lista:
        print(element)

a=[1,2,3]
b=a
print(a)
print(b)
print(id(a))
print(id(b))

c = [a,b]
print(c)

a.append(5)
print(a)
print(b)
print(c)

print('---------------------------------------------------------------------------')

a= [1,2,3]
id(a)
print(id(a))
b=a
id(b)
print(id(b))
c= list(a)
print(c)
print(id(c))

d= a[::]
print(d)
print(id(d))


lista = list(range(1000))
print(lista)

doble = [i*2 for i in lista]
print(doble)

pares = [i for i in lista if i%2==0]
print(pares)