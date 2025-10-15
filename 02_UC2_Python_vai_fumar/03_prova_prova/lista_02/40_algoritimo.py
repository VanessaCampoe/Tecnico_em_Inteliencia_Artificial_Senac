# Algoritmo 40 – Entrar com dois números inteiros e imprimir a seguinte saída: Dividendo, Divisor, Quociente, Resto
dividendo = int(input("Digite o dividendo (número inteiro): "))
divisor = int(input("Digite o divisor (número inteiro): "))
quociente = dividendo // divisor
resto = dividendo % divisor
print("Dividendo:", dividendo)
print("Divisor:", divisor)
print("Quociente:", quociente)
print("Resto:", resto)
