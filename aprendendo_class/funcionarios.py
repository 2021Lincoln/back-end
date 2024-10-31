

"""

Uma clinica deseja criar um sistea para cadastrar seus funcionarios, medicos e enfermeiro. o sistema também deverá mostrar 
as especialidades que os medicos atendem na clinicae os dias de atendimento dos mesmos
Criar uma classe funcionario com os seguintes atributos: matricula, nome, telefone, email, cpf e rg. A empresa também necessita que seja criadas AS SUBCLASSES
para os medicos e enfermeiros. Os enfermeiros possuem documentação da classe: COREN e os médicos possuem seu CRM.

Criar as classes, subclasses e criar objetos para os mesmos.
A subclasse medico deve conter o metodo atende onde sempre que  for chamado exibir as especialidades e os horários que o medico atende.

Solicitar a digitação dos dados, salvar em uma lista e ao final exibir todos os funcionários

"""


class Funcionarios:
    def __init__(self, matricula, nome, telefone, email, cpf, rg, cargo):
        self.matricula = matricula
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.rg = rg
        self.cargo = cargo




