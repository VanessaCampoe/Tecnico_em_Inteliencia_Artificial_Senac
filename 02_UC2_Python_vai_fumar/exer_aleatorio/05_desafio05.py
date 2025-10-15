""" cadastrar 7um produto e descobir seu valor total """
# string[e  ] texto 
produto = input("Digite o nome do produto")
qtde = int(input("Digite a quantidade de produto"))
preco = float(input("Digite o valor do preço"))
#  aqu8i voce coloca o typo no  caso float q e um decimal 
total = qtde * preco
print('o valor total:', total) # concatenar
print(f"o produto {produto} tem valor total de {total}") # interpolar

# verificacao logica 
#  estrutura condicional
#Se o valor total for acima de mil reais me de o desconto de 10%
# operadores relacionais 

if total >= 1000: 
    print ("O valor total [e] maior ou igual a 1000") 



#  erro foi nao entrar na pasta certa 

"""
🔢 1. Números Naturais (ℕ)

São os números usados para contar.

📌 Exemplos:
0, 1, 2, 3, 4, 5, ...

➗ 2. Números Racionais (ℚ)

São todos os números que podem ser escritos como fração entre dois inteiros, com denominador diferente de zero.

📌 Exemplos:

1/2, -3/4, 7 (pois 7 = 7/1), 0, -5, 0.25 (pois 0.25 = 1/4)

3. Números Reais (ℝ)

É o conjunto mais completo entre os três.

Os números reais incluem:

Naturais (ℕ)

Inteiros (ℤ)

Racionais (ℚ)

Irracionais (números que não podem ser escritos como fração, como √2, π, e)

📌 Exemplos:

2, -7, 3/5, 0.75, √2, π

"""
#  