#definición

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self, otra_persona):
        print(f'Hola {otra_persona.nombre}, me llamo {self.nombre} ')

#uso
david = Persona('David',35)
erika = Persona('Erika',32)

david.saluda(erika)