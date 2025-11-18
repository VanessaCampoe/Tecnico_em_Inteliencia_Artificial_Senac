# O MAIN AQUI VAI REPRESENTAR UMA CLASSE     
print("Alo mundo POO!")

from personagem import Personagem
from restaurante import Restaurante

print("""
███╗░░░███╗░█████╗░██╗░░██╗███████╗  ██████╗░██╗███████╗███████╗░█████╗░
████╗░████║██╔══██╗██║░██╔╝██╔════╝  ██╔══██╗██║╚════██║╚════██║██╔══██╗
██╔████╔██║███████║█████═╝░█████╗░░  ██████╔╝██║░░███╔═╝░░███╔═╝███████║
██║╚██╔╝██║██╔══██║██╔═██╗░██╔══╝░░  ██╔═══╝░██║██╔══╝░░██╔══╝░░██╔══██║
██║░╚═╝░██║██║░░██║██║░╚██╗███████╗  ██║░░░░░██║███████╗███████╗██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝""")
print("1. cadastrar pizzaria")
print("2. listar pizzaria")
print("3. ativar pizzaria")
print("4. sair pizzaria")
opcao = int(input("Escolher uma opçao:"))
 # https://fsymbols.com/pt/
print("Quais os dados do personagem ")



p1 = Personagem (nome="Enzo",
                            idade=17,
                            altura=1.75,
                            peso=70, cor="pardo") 
# obejto e uma instacia da classe 
#p1 e um objeto da classe Personagem  
print(f"O nome do personagem é {p1.nome}")
print(f"O idade do personagem é {p1.idade}")
print(f"O altura do personagem é {p1.altura}")
print(f"O peso do personagem é {p1.peso}")
print(f"O cor do personagem é {p1.cor}")






p2 = Restaurante (nome="PizzaTIa", tipo="classica", avaliacao=5, preco="medio")

print(f"{p2.nome}")
print(f"{p2.tipo}")
print(f"{p2.avaliacao}")
print(f"{p2.preco}")