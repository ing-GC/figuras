import math


class calcularArea():
    def __init__(self):
        self.resultado = 0

    def cuadrado(self, a):
        self.resultado = a * a
        return self.resultado

    def rectangulo(self, a, b):
        self.resultado = a * b
        return self.resultado

    def trinagulo(self, b, h):
        self.resultado = (b * h) / 2
        return self.resultado

    def circulo(self, r):
        self.resultado = pow(math.pi * r, 2)
        return self.resultado
