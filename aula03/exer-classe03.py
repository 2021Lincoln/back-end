

#Abaixo foi criado uma classe produtos
class Produto:
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



produtos = []

while True:
    tipo = input("Para cadastrar pressione qualquer tecla ou Digite S para sair: ")

    if tipo.upper() == 'S':
        break

    codProduto = input("Digite o codigo do produto: ")
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")
    tamanho = input("Digite o tamanho do produto: ")
    preco = input("Digite preço do produto: ")

    produto = Produto(codProduto, nome, descricao, tamanho, preco)

    produtos.append(produto)

print("Lista de Produtos: ")
for prod in produtos:
    print(f"Codigo: {prod.codProduto}, '-', Nome do produto: {prod.nome}, '-', descrição: {prod.descricao}, '-', tamanho: {prod.tamanho}, '-', preço: {prod.preco}")



