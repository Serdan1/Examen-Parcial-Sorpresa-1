# punto.py
import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "Está en el origen"
        elif self.x == 0 and self.y != 0:
            return "Está sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Está sobre el eje X"
        elif self.x > 0 and self.y > 0:
            return "Está en el primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Está en el segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Está en el tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Está en el cuarto cuadrante"
    
    def vector(self, otro_punto):
        vector_x = otro_punto.x - self.x
        vector_y = otro_punto.y - self.y
        return Punto(vector_x, vector_y)
    
    def distancia(self, otro_punto):
        dx = otro_punto.x - self.x
        dy = otro_punto.y - self.y
        return math.sqrt(dx**2 + dy**2)