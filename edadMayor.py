print("Progama que calcula la Edad Mayor")
print("Primera Persona")
nombre1 = input("Ingrese su nombre : ")
edad1 = int(input("Ingrese su edad : "))
print("Segunda Persona")
nombre2 = input("Ingrese su nombre : ")
edad2 = int(input("Ingrese su edad : "))


if edad1 > edad2:
    print(f'{nombre1} es el mayor')
elif edad2 > edad1:
    print(f'{nombre2} es el mayor')
else:
    print(f'{nombre1} y {nombre2} tienen la misma edad')