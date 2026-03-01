#ejercicio 2 actividad 2
from enum import Enum

class tipoPlaneta(Enum):
    gaseoso = "gaseoso"
    terrestre = "terrestre"
    enano = "enano"
    
class Planeta:

    def __init__(self, nombre, cantidad_satelites, masa, volumen, diametro, distancia, tipo, observable):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia = distancia
        self.tipo = tipo
        self.observable = observable

    def imprimir(self):
        print("Nombre =", self.nombre)
        print("Cantidad de Satelites =", self.cantidad_satelites)
        print("Masa =", self.masa)
        print("Volumen =", self.volumen)
        print("Diametro =", self.diametro)
        print("Distancia media =", self.distancia)
        print("Tipo de planete =", self.tipo)
        print("Es observable =", self.observable)

    def calcular_densidad(self):
        return self.masa / self.volumen
    
    def calcular_planeta_exterior(self):
        limite = 149597870 * 3.4
        return self.distancia > limite

    
planeta1 = Planeta("Tierra", 1, 5.9736E24, 1.08321E12, 12742, 150000000, tipoPlaneta.terrestre, True)
planeta2 = Planeta("Jupiter", 79, 1.899E27, 1.431E15, 139820, 750000000, tipoPlaneta.gaseoso, True)

planeta1.imprimir()
print("La densidad del planeta es = ", planeta1.calcular_densidad)
print("El planeta es exterior = ", planeta1.calcular_planeta_exterior)
print()

planeta2.imprimir()
print("La densidad del planeta es = ", planeta2.calcular_densidad)
print("El planeta es exterior = ", planeta2.calcular_planeta_exterior)
print()