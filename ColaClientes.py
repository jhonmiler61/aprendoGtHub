
clientes ={
    'angiela' : 3550,
    'iris' : 500,
    'urus' : 800,
    'darwin' : 965,
    'miler': 4500,
}

clientes['mocito'] =500
validar = False
print('----Bienvenido------')
print('')
nombre_cliente = input("Ingrese su nombre : ")
for cliente in clientes.keys():
    if nombre_cliente==cliente:
        validar = True
    
print('--------------')
if validar ==True:
    print(f'Bienvenido {nombre_cliente}')
    print(f'Su saldo actual es {clientes[nombre_cliente]}')

menu_cliente = 0
while menu_cliente !=3:
    print("Selecciona La Operación que desea Realizar")
    print(" 1 : Retirar Dinero")
    print(" 2 : Depositar Dinero")
    print(" 3 : Salir")
    menu_cliente = int(input("Ingrese el numero de Operacion : "))
    if menu_cliente==1:
        print('-------Retiro de dinero---------')
        cantidad_retiro = int(input('Cantidad que desea retirar: '))
        print(f'---Usted retiro {cantidad_retiro}')
        clientes[nombre_cliente] = clientes[nombre_cliente] - cantidad_retiro
        print(f'El saldo de su cuenta es {clientes[nombre_cliente]}')
        print('------------------------------')

    elif menu_cliente==2:
        print("-------Deposito de Dinero --------")
        cantidad_deposito = int(input('Cantidad que desea depositar: '))
        print(f'Usted esta depositando {cantidad_deposito}')
        clientes[nombre_cliente] = clientes[nombre_cliente] + cantidad_deposito
        print(f'El saldo de su cuenta es {clientes[nombre_cliente]}')
        print('------------------------------')
    
    elif menu_cliente==3:
        print("Saliendo ....")



