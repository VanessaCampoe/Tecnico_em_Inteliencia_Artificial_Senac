# Algoritmo 41 – Entrar com quatro números e imprimir a média ponderada, sabendo-se que os pesos são respectivamente: 1, 2, 3 e 4.
n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))
n3 = float(input("Digite o 3º número: "))
n4 = float(input("Digite o 4º número: "))
media_ponderada = (n1*1 + n2*2 + n3*3 + n4*4) / (1+2+3+4)
print("Média ponderada:", media_ponderada)



