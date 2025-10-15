# Digite  a área de desmatamento: 
# Area desmatada: xxxxx
# Equivalente  a xxxxx campos de futebol (arrendondado) - use funcao round( )
# Mas precisamente :   xxxxxxx campos

# use as funções: pow(2,2) e round( ) ou o operador **

area_desmatada = float(input("Digite a area desmata em km²"))


print(f" a area dematada é : {area_desmatada} km²")
# Entrada do usuário
area_desmatada = float(input("Digite a área de desmatamento em km²: "))

# Cálculos
area_m2 = area_desmatada * 1_000_000  # converte km² para m²
campo_m2 = 100 * 60                   # área de um campo de futebol (100m x 60m)
num_campos = area_m2 / campo_m2

# Saída formatada
print(f"\nÁrea desmatada: {area_desmatada} km²")
print(f"Equivalente a {round(num_campos)} campos de futebol (arredondado)")
print(f"Mais precisamente: {num_campos:.2f} campos")

