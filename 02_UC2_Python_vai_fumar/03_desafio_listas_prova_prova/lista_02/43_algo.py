# Algoritmo 43 – Entrar com um número e imprimir o logaritmo desse número na base 10.
num = float(input("Digite um número para calcular o logaritmo base 10: "))
if num > 0:
    log10 = math.log10(num)
    print(f"Logaritmo base 10 de {num} é {log10}")
else:
    print("Número inválido para cálculo de logaritmo.")