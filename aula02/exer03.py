"""
Faça um programa que calcule o desconto de uma compra feita em uma loja. 
O programa deve ler o valor das compras e calcular o valor do desconto obedecendo os seguintes percentuais:

10% de desconto se a compra for menor ou igual que 2.000
5% de descont se a compra for maior que 2.000 e menor ou igual a 3.000
3% de desconto se for maior que 3.000 e menor ou igual a 5.000
2% de desconto para compras acima de 5.000

O programa deverá exibir ao final: o valor da compra do desconto e o total a pagar 


"""

valor_compra = float(input("Digite o valor da compra: "))

if valor_compra <= 2000:
    desconto = (valor_compra * 0.10)
    total =  valor_compra - desconto
    print(f"O valor da compra com 10% de desconto R$ {total}")
elif valor_compra > 2000 and valor_compra <= 3000:
    desconto = (valor_compra * 0.5)
    total = valor_compra - desconto
    print(f"O valor da compra com 5% de desconto R$ {total}")
elif valor_compra > 3000 and valor_compra <= 5000:
    desconto = (valor_compra * 0.3)
    total = valor_compra - desconto
    print(f"O valor da compra com 3% de desconto R$ {total}")
elif valor_compra > 5000:
    desconto = (valor_compra * 0.2)
    total = valor_compra - desconto
    print(f"O valor da compra com 2% de desconto R$ {total}")
