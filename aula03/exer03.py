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



alunos = [
    {"nome": "Alice", "nota": 8},
    {"nome": "Bob", "nota": 7},
    {"nome": "Carol", "nota": 9},
    {"nome": "David", "nota": 6}
]


# chamanddo a função para calcular a media das notas
media_notas = calcular_media_alunos(alunos)
print(f"Média da turma: {media_notas}")


