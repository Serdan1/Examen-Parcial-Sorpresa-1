# main.py
from punto import Punto
from rectangulo import Rectangulo

# Crear los puntos A, B, C y D e imprimirlos
A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

print("Puntos creados:")
print(f"Punto A: {A}")
print(f"Punto B: {B}")
print(f"Punto C: {C}")
print(f"Punto D: {D}")
print()

# Consultar los cuadrantes de A, C y D
print("Cuadrantes:")
print(f"Punto A: {A} -> {A.cuadrante()}")
print(f"Punto C: {C} -> {C.cuadrante()}")
print(f"Punto D: {D} -> {D.cuadrante()}")
print()

# Consultar los vectores AB y BA
vector_AB = A.vector(B)
vector_BA = B.vector(A)
print("Vectores:")
print(f"Vector AB: {vector_AB}")
print(f"Vector BA: {vector_BA}")
print()

# Consultar la distancia entre A y B, y B y A
distancia_AB = A.distancia(B)
distancia_BA = B.distancia(A)
print("Distancias:")
print(f"Distancia de A a B: {distancia_AB}")
print(f"Distancia de B a A: {distancia_BA}")
print()

# Determinar cuál de los puntos A, B o C está más lejos del origen
origen = Punto(0, 0)
distancia_A = A.distancia(origen)
distancia_B = B.distancia(origen)
distancia_C = C.distancia(origen)

print("Distancias al origen:")
print(f"Distancia de A{origen}: {distancia_A}")
print(f"Distancia de B{origen}: {distancia_B}")
print(f"Distancia de C{origen}: {distancia_C}")

distancias = {
    "A": distancia_A,
    "B": distancia_B,
    "C": distancia_C
}
punto_mas_lejano = max(distancias, key=distancias.get)
distancia_mas_lejana = distancias[punto_mas_lejano]
print(f"El punto más lejano del origen es {punto_mas_lejano}{globals()[punto_mas_lejano]} con una distancia de {distancia_mas_lejana}")
print()

# Crear un rectángulo con los puntos A y B
rectangulo = Rectangulo(A, B)

# Consultar base, altura y área del rectángulo
print("Rectángulo:")
print(rectangulo)
print(f"Base del rectángulo: {rectangulo.base()}")
print(f"Altura del rectángulo: {rectangulo.altura()}")
print(f"Área del rectángulo: {rectangulo.area()}")