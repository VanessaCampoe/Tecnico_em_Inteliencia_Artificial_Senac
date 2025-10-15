# Algoritmo 42 – Entrar com um ângulo em graus e imprimir: seno, co-seno, tangente, secante, co-secante e co-tangente deste ângulo. Use o módulo math.
import math
angulo_graus = float(input("Digite um ângulo em graus: "))
angulo_rad = math.radians(angulo_graus)  # converter para radianos

seno = math.sin(angulo_rad)
coseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)
secante = 1 / coseno if coseno != 0 else float('inf')
cossecante = 1 / seno if seno != 0 else float('inf')
cotangente = 1 / tangente if tangente != 0 else float('inf')

print(f"Seno: {seno}")
print(f"Coseno: {coseno}")
print(f"Tangente: {tangente}")
print(f"Secante: {secante}")
print(f"Cossecante: {cossecante}")
print(f"Cotangente: {cotangente}")


