# rectangulo.py
import math
from punto import Punto

class Rectangulo:
    def __init__(self, inicial=None, final=None):
        self.inicial = inicial if inicial is not None else Punto(0, 0)
        self.final = final if final is not None else Punto(0, 0)
    
    def base(self):
        return abs(self.final.x - self.inicial.x)
    
    def altura(self):
        return abs(self.final.y - self.inicial.y)
    
    def area(self):
        return self.base() * self.altura()
    
    def __str__(self):
        return f"Rectángulo con diagonal desde {self.inicial} hasta {self.final}"