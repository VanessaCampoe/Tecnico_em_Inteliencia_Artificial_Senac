# a classe e um conjunto de obejto 
# metodos espéciais (dunder methods)
#__init__ e o construtor da classe 
# consturi o obejeto da memoria ]
#Stadfck e a pilha de chamadas 
# heap e a memoria dinamica 
# sel serve para definir os atributos do objetivo 

#__init __ methodo especial  posso chamar de super mem pq tras poderes incriveis 
class Mercado:
    def __init__(self, nome, midia, ativo):
        self.nome = nome
        self.midia = midia
        self.ativo = ativo  
        
        # variavael temporaia para passar o valor , isso estas depois do igual 

    def ativar(self):
        self.ativo = True 

    def desativar (self):
        self.ativo = False
        
    def __str__(self):
        # retorna as caracterristica do objeto 
        return f"O mercado {self.nome} esta  {'ativo' if self.ativo else 'inativo'}."
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        