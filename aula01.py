"""Programa 1"""
#Por padrão as strings serão exibidos com um espaço em branco entre elas
"""
print("Isso", "é", "um", "teste")

#Pular \n linha na mensagem
print("Essa mensagem aparece na primeira linha\nEnquanto essa aparece na segunda")

x = 10
#Print com separador _entre os valores a serem exibidos
print("O quadrado do numero", x, "é igual a", x**2, sep="_")

#Usando o end para não pular a linha após o print
print("Vou imprimir isso em uma linha ", end=' ')
print("Continuarei na linha de cima")
"""


"""Programa 2"""
#Faça um programa para somar 2 numeros.

""" 
numero1 = int(input("Digite um numero inteiro: "))
numero2 = int(input("Digite outro numero inteiro: "))

soma = numero1 + numero2

print("A soma de ", numero1, "+", numero2, "=", soma)

#Faça um programa que peça o raio de um circulo, calcule e mostre sua area.
#(área do circulo = pii X raio² e pii = 3.1415)


raio = float(input("Digite o raio do circulo: "))
area = 3.1415 * raio**2
print("O circulo de raio", raio, "tem area igual a", area)
"""


"""Programa 3"""
"""
#Faça um programa que peça a temperatura em graus fahrenheit, transforme e mostre a temperatura em graus Celsius.

temp = float(input("Digite a temperatura em graus fahrenheit: "))
calc = 5*(temp-32)/9

print(f"Resultado da temperatura em graus celsiu é: {calc:.2f}")
"""

"""Programa 4"""
#Faça um programa que peça dois numeros inteiros e um numero real. calcule e mostre:

"""
A) O produto do dobro do primeiro com a metade do segundo.
B) A soma do triplo do primeiro com o terceiro
C) O terceiro elevado ao cubo
"""
"""
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
numReal = float(input("Digite um numero real: "))

n1 = (num1 * 2) * (num2 / 2)
n2 = (num1 * 3) + num2
n3 = numReal**2
print(f"O produto do dobro do primeiro com a metade do segundo {n1}")
print(f"A soma do triplo do primeiro com o terceiro {n2}")
print(f"O numero real elevado ao cubo {n3}")
"""

"""Programa 5"""

"""
Faça um programa que leia o salario de uma pessoa em um determinado mês. calcule e mostre o seu salario liquido no referido mês,
sabendo-se que são descontados 11% para o imposto de renda, 8% para o inss e 5% para o sindicato. A saida do programa deve escrever o seguinte:
(+) salario bruto:R$ valor
(-) Ir(11%):R$ valor
(-) Inss(8%):R$ valor
(-) Sindicato(5%):R$ valor
(-) Total desconto:R$ valor
(=) salario liquido:R$ valor

Obs: Sálario liquido = salario bruto - descontos

"""

"""
ir = 11
inss = 8
sindicato = 5


salario = float(input("Digite o valor do salario do mês: "))

valor_ir = (ir/100) * salario
valor_inss = (inss/100)*salario
valor_sindicato = (sindicato/100)*salario

desc_total = valor_ir + valor_inss + valor_sindicato

total = salario - desc_total
print(f"o desconto de imposto de renda é de: {valor_ir:.2f}")
print(f"O desconto do inss é de: {valor_inss}")
print(f"O desconto do sindicato é de: {valor_sindicato}")
print(f"O valor total dos descontos é de: {desc_total}")
print(f"Seu salário liquido é: {total}")

"""




"""Programa 6"""
"""
A padaria Sópão vende diariamente uma certa quantidade de pães franceses e uma quantidade de broas.
Cada pãozinho custa R$ 0,80 e a broa custa R$2,50. do total arrecadado, 43% corresponde aos custos da fabricação.
Do restante, seu joão guarda 15% numa conta de poupança e 15% ele converte em
Euros para viagem anual. sabe-se que 1 Euro custo R$ 4,60. Com base nestes fatos, faça um programa 
para ler as quantidades de pães e de broas, calcular a venda total de pães e broas, custo de fabricação,
quanto irá guardar na poupança e quantos Euros irá comprar. ao final exibir os dados calculados.


"""

continuar = "S"

pao = 0.80
broa = 2.50

custos_fabricacao = 

poupanca = (15/100)*

viagem = (15/100)*4.60

while continuar == "S":

    qtd_paes = int(input("Qual a quantidade de pães: "))

    qtd_broas = int(input("Qual a quantidade de broas: "))

    continuar = input("Deseja mais alguma coisa? (S-sim/N-nao)")















"""Programa 7"""
"""
Faça um programa para calcular a quantidade de latas de tintas para pintar um parede. o programa 
deverá solicitar ao usuario, a altura (float) e o comprimento(float) da parede. Considere que a cobertura
da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 3,6 litros, que 
custam R$107,00. informe ao usuario a quantidade de latas de tinta a serem compradas e o preço total.

altura = float(input(""))
comprimento = float(input(""))

area = altura * comprimento

litros_necessario = match.ceil(litros_necessarios / )




"""


""" Programa 8 """
"""
Um determinado prêmio da loteria saiu um bolão

"""