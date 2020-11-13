diccionario ={
    'miler':22,
    'angiela':20,
    'iris':0,
}

print(diccionario['miler'])
diccionario['miler']
print(diccionario)

del diccionario['iris']
print(diccionario)

for llave in diccionario.keys():
    print(llave)

for valor in diccionario.values():
    print(valor)

for llave, valor in diccionario.items():
    print(llave, valor)

print('miler' in diccionario)