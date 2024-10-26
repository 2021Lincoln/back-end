"""Utilizado dicionario de dados em lista    ****Importante essa parte"""

pessoas = [{"nome": "joão", "idade": 25},
            {"nome": "Maria", "idade": 30},
            {"nome": "Pedro", "idade": 28},
            {"nome": "Ana", "idade": 22}]

#Acessando os elementos da lista
for pessoa in pessoas:
    nome = pessoa["nome"]
    idade = pessoa["idade"]
    print(f"Nome: {nome}, idade: {idade}")



"""for pessoa in pessoas:
    print(f"Nome: ", pessoa["nome"], pessoa["idade"])   Aqui estou chamando diretamente"""

