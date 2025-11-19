# se eu progamo sem poo , eu sou um programdar pprocidural ]
# funoes soltas , estruturas sequenciais e dicionarios 

from mercado import Mercado 
# criar um dicionario mercado : nome . sites produtos 
mercado = {
    "nome": "Tudo bem ",
    "midia": "www.tudobom.com.br",
    "ativo": False

}
# Paradiugma procedual
 # paradgima orientado a obejto 
 # paradigima  funcional (lambida )_
 m1 = Mercado("Tudo bom " False)
 m2 = Mercado("compra facil ", "www.comprafacil.com.br",True)
 m3 = Mercado("Mercado legal ","www.mercadolegal.com.br", False)
 m4 = Mercado("Supermercado Show ", "www.supernaercadoshow.com.br", True)
 
 # obejto = Muinha classe construtora  
 
 print(m1.ativo)
 m1.ativar()
 # aqui meu objeto m1 
 print(m1.active_count)
 
 mercado = [m1 , m2 , m3 , m4 ]
 pritn("lista de mercado")
 for mercado in mercados:
    status - "Ativo " if mercado.ativo else "Inativo" 
    print(f"{mercado.nome}, Site:{mercado.midia}, Status: {status}")
    
print(vars(m1)) # lista o conteudo do objeto ou um bug

print(dir(m1))

print(str(m1))