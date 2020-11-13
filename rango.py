my_range = range(1,5)
type(my_range)
for i in my_range:
    print(i)

mi_rango = range(0,7,2)
otro_rango = range(0,8,2)
print(f'--------------')

mi_rango == otro_rango

for i in mi_rango:
    print(i)
print(f'------operador de igualdad simple--------')

for i in otro_rango:
    print(i)

print(f'-----Operado de igualdad de objetos---------')
print(mi_rango is otro_rango)
print(f'-------------')

for i in range(0,101,2):
    print(i)
