"""Dadas as informações dos produtos de uma loja, crie uma lista dicionarizada para guardar os elementos 
 fornecidos e em seguida crie uma função que receba a lista e a imprime
 
 Dados:
 Produto: tv 50 polegadas - marca: samsung
 produto: micro-ondas 10 litros - marca: panasonic,
 produto: Iphone 15 pro max - marca Apple,
 produto: smartphone redmi note 13 - marca: xiaomi,
 produto: lavadora 10 kg - marca: brastemp """


#Lista dicionarizada, Ou seja abaixo está sendo criado um dicionario em python
produtos = [
 {"produto": "tv 50 polegadas", "marca": "samsung"},
 {"produto": "micro-ondas 10 litros", "marca": "panasonic"},
 {"produto": "Iphone 15 pro max", "marca": "Apple"},
 {"produto": "smartphone redmi note 13","marca": "xiaomi"},
 {"produto": "lavadora 10 kg", "marca": "brastemp"
}]

#Abaixo foi criado uma função com um for para pegar cada elemento da lista e printar na tela
def imprimir(produtos):
    for produto in produtos:
        print(f"Produto: {produto['produto']}, Marca: {produto['marca']}")


#Abaixo está sendo chamado a função passando o parametro produtos
imprimir(produtos)
