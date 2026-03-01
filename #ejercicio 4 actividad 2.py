#ejercicio 4 actividad 2
import math
class circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def areaCirculo(self):
        return math.pi * math.pow(self.radio, 2)
    
    def perimetroCirculo(self):
        return 2 * math.pi * self.radio


class rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def areaRectangulo(self):
        return self.base * self.altura
    
    def perimetroRectangulo(self):
        return (2*self.base)+(2*self.altura)

class cuadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def areaCuadrado(self):
        return self.lado * self.lado
    
    def perimetroCuadrado(self):
        return 4 * self.lado


class trianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def areaTriangulo(self):
        return (self.base * self.altura) / 2
    
    def calcularHipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)
    
    def perimetroTriangulo(self):
        return (self.base + self.altura + self.calcularHipotenusa())
    
    def tipoTriangulo(self):
        hipotenusa = self.calcularHipotenusa()
        
        if self.base == self.altura == hipotenusa:
            print("Es un triangulo equilatero")
        elif self.base != self.altura and self.base != hipotenusa and self.altura != hipotenusa:
            print("Es un triagulo escaleno")
        else:
            print("Es un triangulo isosceles")

class rombo:
    def __init__(self, diagonal_mayor, diagonal_menor, lado):
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor
        self.lado = lado
    
    def areaRombo(self):
        return (self.diagonal_mayor * self.diagonal_menor) / 2
    
    def perimetroRombo(self):
        return 4 * self.lado
    
class trapecio:
    def __init__(self, base_mayor, base_menor, lado1, lado2, altura):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.lado1 = lado1
        self.lado2 = lado2
        self.altura = altura
    
    def areaTrapecio(self):
        return ((self.base_mayor + self.base_menor) * self.altura) / 2
    
    def perimetroTrapecio(self):
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2


radio = float(input("Ingrese el radio del circulo: "))
base_rect = float(input("Ingrese la base del rectangulo: "))
altura_rect = float(input("Ingrese la altura del rectangulo: "))
lado_cuad = float(input("Ingrese el lado del cuadrado: "))
base_tri = float(input("Ingrese la base del triangulo rectangulo: "))
altura_tri = float(input("Ingrese la altura del triangulo rectangulo: "))
diag_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
diag_menor = float(input("Ingrese la diagonal menor del rombo: "))
lado_rombo = float(input("Ingrese el lado del rombo: "))
base_mayor_trap = float(input("Ingrese la base mayor del trapecio: "))
base_menor_trap = float(input("Ingrese la base menor del trapecio: "))
lado1_trap = float(input("Ingrese el lado 1 del trapecio: "))
lado2_trap = float(input("Ingrese el lado 2 del trapecio: "))
altura_trap = float(input("Ingrese la altura del trapecio: "))


circulo1 = circulo(radio)
rectangulo1 = rectangulo(base_rect, altura_rect)
cuadrado1 = cuadrado(lado_cuad)
triangulo1 = trianguloRectangulo(base_tri, altura_tri)
rombo1 = rombo(diag_mayor, diag_menor, lado_rombo)
trapecio1 = trapecio(base_mayor_trap, base_menor_trap, lado1_trap, lado2_trap, altura_trap)

print(f"El area del circulo es: {circulo1.areaCirculo()}")
print(f"El perimetro del circulo es: {circulo1.perimetroCirculo()}")
print()
print(f"El area del rectangulo es: {rectangulo1.areaRectangulo()}")
print(f"El perimetro del rectangulo es: {rectangulo1.perimetroRectangulo()}")
print()
print(f"El area del cuadrado es: {cuadrado1.areaCuadrado()}")
print(f"El perimetro del cuadrado es: {cuadrado1.perimetroCuadrado()}")
print()
print(f"El area del triangulo es: {triangulo1.areaTriangulo()}")
print(f"El perimetro del triangulo es: {triangulo1.perimetroTriangulo()}")
triangulo1.tipoTriangulo()
print()
print(f"El area del rombo es: {rombo1.areaRombo()}")
print(f"El perimetro del rombo es: {rombo1.perimetroRombo()}")
print()
print(f"El area del trapecio es: {trapecio1.areaTrapecio()}")
print(f"El perimetro del trapecio es: {trapecio1.perimetroTrapecio()}")
print()