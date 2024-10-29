

#Abaixo foi criado uma classe produtos
class Produtos:
    def __init__(self, codProduto, nome, descricao, tamanho, preco): #Nesta linha foi criado os atributos da classe

        self.codProduto = codProduto  #Nas linhas abaixo foi criado uma referenciação ao atributo da classe
        self.nome = nome
        self.descricao = descricao
        self.tamanho = tamanho
        self.preco = preco

    def calcular(self): #Nesta linha foi criado uma função para calcular o desconto
        desconto = self.preco * 0.10 #Aqui foi criado uma variavel para armazenar o desconto em cima 
        preco_com_desconto = self.preco - desconto

        print(f"você obteve um desconto de 10%")
        print(f"O preço com desconto: {preco_com_desconto}")




produto1 = Produtos('0021', 'celular', 'eletronico', '2', 500)
produto2 = Produtos('0022', 'capinha de celular', 'capa', '15cm', 25)
produto3 = Produtos('0023', 'carregador de celular', 'eletronico', '3cm', 40)


produto1.calcular()
print(f"O codigo do produto é {produto1.codProduto}")
print(f"O nome do produto é {produto1.nome}")
print(f"A descrição do produto é {produto1.descricao}")
print(f"O tamanho do produto é {produto1.tamanho}")
print(f"O preço do produto é {produto1.preco}\n")



produto2.calcular()
print(f"O codigo do produto é {produto2.codProduto}")
print(f"O nome do produto é {produto2.nome}")
print(f"A descrição do produto é {produto2.descricao}")
print(f"O tamanho do produto é {produto2.tamanho}")
print(f"O preço do produto é {produto2.preco}\n")


produto3.calcular()
print(f"O codigo do produto é {produto3.codProduto}")
print(f"O nome do produto é {produto3.nome}")
print(f"A descrição do produto é {produto3.descricao}")
print(f"O tamanho do produto é {produto3.tamanho}")
print(f"O preço do produto é {produto3.preco}\n")