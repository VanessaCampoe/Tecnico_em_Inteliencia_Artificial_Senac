# Algoritmo 41 – Entrar com quatro números e imprimir a média ponderada, sabendo-se que os pesos são respectivamente: 1, 2, 3 e 4.
n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))
n3 = float(input("Digite o 3º número: "))
n4 = float(input("Digite o 4º número: "))
media_ponderada = (n1*1 + n2*2 + n3*3 + n4*4) / (1+2+3+4)
print("Média ponderada:", media_ponderada)


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


# Algoritmo 43 – Entrar com um número e imprimir o logaritmo desse número na base 10.
num = float(input("Digite um número para calcular o logaritmo base 10: "))
if num > 0:
    log10 = math.log10(num)
    print(f"Logaritmo base 10 de {num} é {log10}")
else:
    print("Número inválido para cálculo de logaritmo.")
