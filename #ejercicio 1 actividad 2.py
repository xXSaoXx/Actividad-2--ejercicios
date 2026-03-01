#ejercicio 1 actividad 2
class Persona():
    def __init__(self, nombre, apellido, id, fecha_nacimiento, pais, genero):
        if genero not in ("H", "M"):
            raise ValueError("El genero debe ser 'H' o 'M'")
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.fecha_nacimiento = fecha_nacimiento
        self.pais = pais
        self.genero = genero

    def imprimir(self):
        print("Nombre  = ", self.nombre)
        print("Apellido  = ", self.apellido)
        print("Documento = ", self.id)
        print("Año de nacimiento  = ", self.fecha_nacimiento)
        print("País de nacimiento = ", self.pais)
        print("Genero = ", self.genero)
        print()


p1 = Persona("Juan", "Tabarez", "7592", "17 de febrero de 2000", "Peru", "H")
p2 = Persona("María", "Escobar", "1234", "8 de octubre de 2002", "España", "M")

p1.imprimir()
p2.imprimir()