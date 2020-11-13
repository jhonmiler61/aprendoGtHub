
clientes ={
    'angiela' : 3550,
    'iris' : 500,
    'urus' : 800,
    'darwin' : 965,
    'miler': 4500,
}

programa_activo= True

def atender_cliente():
    """Funcion Atender al clientes"""
    validar = False
    print()
    print("..................................")
    print('----Bienvenido Cliente------')
    nombre_cliente = input("Ingrese su nombre : ")
    for cliente in clientes.keys():
        if nombre_cliente==cliente:
            validar = True
    print()
    print('--------------')
    if validar ==True:
        print(f'Bienvenido {nombre_cliente}')
        print(f'Su saldo actual es {clientes[nombre_cliente]}')
    else:
        print("Cliente no registrado !")
        return

    menu_cliente = 0
    while menu_cliente !=3:
        print()
        print("Selecciona La Operación que desea Realizar")
        print(" 1 : Retirar Dinero")
        print(" 2 : Depositar Dinero")
        print(" 3 : Salir")
        menu_cliente = int(input("Ingrese el numero de Operacion : "))
        if menu_cliente==1:
            print()
            print('-------Retiro de dinero---------')
            cantidad_retiro = int(input('Cantidad que desea retirar: '))
            print(f'---Usted retiro {cantidad_retiro}')
            clientes[nombre_cliente] = clientes[nombre_cliente] - cantidad_retiro
            print(f'{nombre_cliente}: El saldo de su cuenta es {clientes[nombre_cliente]}')
            print('------------------------------')

        elif menu_cliente==2:
            print()
            print("-------Deposito de Dinero --------")
            cantidad_deposito = int(input('Cantidad que desea depositar: '))
            print(f'Usted esta depositando {cantidad_deposito}')
            clientes[nombre_cliente] = clientes[nombre_cliente] + cantidad_deposito
            print(f'{nombre_cliente}: El saldo de su cuenta es {clientes[nombre_cliente]}')
            print('------------------------------')
        
        elif menu_cliente==3:
            print()
            print("Saliendo ....")


def abrir_cuenta():
    """Funcion crear nueva cuenta"""
    print()
    print("------------------------------")
    print("---------Abrir Cuenta---------")
    print("------------------------------")
    cliente_nuevo = input("Ingrese su nombre : ")
    cantidad_a_depositar = int(input("Ingrese la cantidad a depositar: "))
    clientes[cliente_nuevo] = cantidad_a_depositar
    print("...............................")
    print(f' Felicidades {cliente_nuevo}  !!! se creo correctamente tu cuenta')
    print(f' Tu saldo es : {cantidad_a_depositar}')
    print("...............................")





ultimo = 5
cola = list(range(1,ultimo+1))

while programa_activo == True:
    print()
    print("--------- Bienvenido -----------")
    print("Seleccione Operacion a Realizar")
    print("Digite para atender: A")
    print("Digite para agregar Ticket: T")
    print("Digite para salir: S")
    print("----------------------------------")
    print(f' Personas en cola :  {len(cola)}')
    operacion= input("Ingrese la Operacion : ")

    if operacion == "A" or operacion =="a":
        print()
        print("--------------------------------------------")
        print(" ----- Seleccionar Tipo de Atencion ------- ")
        print("--------------------------------------------")
        print(" Atencion a Cliente Registrado : 1 ")
        print(" Abrir Cuenta de Cliente: 2")

        tipo_atencion = int(input(".... Ingresar numero de Operacion : "))
        if tipo_atencion == 1:
            atender_cliente()
        elif tipo_atencion == 2:
            abrir_cuenta()
        else: 
            print(" Finaliza la Atencion .... ")

        atendido=cola.pop(0)
        print (f'Se realizo la atencion del cliente {atendido}')

        
    
    elif operacion =="T" or operacion =="t":
        ultimo = ultimo +1
        cola.append(ultimo)

    elif operacion == "S" or operacion == "s":
        programa_activo = False
        print("Saliendo del Programa ...")
    
    else:
        print("Valor ingresado incorrecto")

    


    

