"""
A escola "APRENDER" faz o pagamento de seus professores por hora/aula mais 
15% do salario referente as descanso semanal remunerado (DSR). Faça um 
programa que leia o nivel do professor  (1 ou 2) e a quantidade de horas de aula
dada no mês, calcule e exiba o salario de um professor. sabe-se que o valor da hora/aula segue a tabela abaixo:

professor nivel 1 R$ 56,00 por hora/aula
professor nivel 2 R$ 66,00 por hora/aula

"""

nivel = int(input("Digite o seu nivel do professor 1 ou 2: "))
horas_aula = float(input("Digite a quantidade de horas aulas dadas no mês: "))


def calc(nivel, horas_aula):
    if nivel == 1:
        salbase = 56 * horas_aula
    elif nivel == 2:
        salbase = 66 * horas_aula
    else:
        print("Nivel inexistente")
        return 0

    dsr = salbase * 0.15

    salario = salbase + dsr

    return salario


print(f"A quantidade de horas a ser recebidas é de: R${calc(nivel, horas_aula)}")

