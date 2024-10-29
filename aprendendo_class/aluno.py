from pessoa import Pessoa


#Abaixo está sendo criado uma outra classe para aluno, onde está sendo herdado de pessoa os atributos e acrescido a matricula

class Aluno(Pessoa):
    def __init__(self, nome, data_nascimento, sexo, matricula): #Aqui nesta linha está sendo criado todos os atributos de pessoa + o atributo novo que é matricula
        super().__init__(nome, data_nascimento, sexo) #Aqui estou dizendo para o programa que os atributos são de "pesssoa"
        self.matricula = matricula #Aqui estou referenciando apenas o atributo novo de aluno, pois não preciso referenciar os outros, pois já foi referenciado lá em cima na outra classe pessoa

aluno1 = Aluno("Lincoln", "30/08/1992", "Masculino", 220023)

print("----------Dados do Aluno---------")
print("Matricula:", aluno1.matricula)
print("Nome:", aluno1.nome)
print("Data de nascimento:", aluno1.data_nascimento)
print("Sexo:", aluno1.sexo)