"""
Uma empresa oferece para os 10 primeiros clientes um determinado desconto de acordo com o valor da compra efetuada.
O desconto é de 20% se o valor da compra for maior ou igual a 1500 reais, e 15% se for menor.
Fazer um programa  que leia de cada cliente o valor da compra e o nome do cliente, calcule o desconto e exiba o nome do cliente, valor da compra,
o desconto e o valor a ser pago. ao final, exibir total de desconto dado aos 10 cliente 

"""

for i in range(10):
    nome = input("Digite seu nome: ")
    valor_compra = int(input("Digite o valor da compra"))

    if valor_compra >= 1500:
        desconto = (valor_compra * 0.20)
        total = desconto - valor_compra
        print(f"Nome do cliente é: {nome}, Valor da compra com desconto {total}")
    contador1 = contador1 + 1
    
    # elif valor_compra < 1500:
    #     desconto = (valor_compra * 0.15)
    #     total = desconto - valor_compra
    # contador2 = contador + 1
    

    