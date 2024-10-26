"""Interessante essa forma que foi descrita o codigo"""



def calcular_media_alunos(alunos):
    soma_notas = 0
    qtd_alunos = len(alunos)

    for aluno in alunos: #aluno está recebendo a quantidade de alunos que tem no array de alunos, o for está pegando aluno por aluno e nota a cada loop
        nome = aluno["nome"]
        nota = aluno["nota"]
        soma_notas += nota
        print(f"Nome: {nome}, Nota: {nota}")

    media = soma_notas / qtd_alunos
    return media #fim da função


alunos = []
qtd_alunos = int(input("Digite a quantidade de alunos: "))

for _ in range(qtd_alunos): #Aqui o _ está assumindo apenas a quantidade que tem na lista de qtd _alunos
    nome = input("Digite seu nome: ")
    nota = int(input("digite a sua nota: "))
    alunos.append({"nome": nome, "nota": nota})

# chamando a função para calcular a media das notas
media_notas = calcular_media_alunos(alunos)
print(f"Média da turma: {media_notas}")
