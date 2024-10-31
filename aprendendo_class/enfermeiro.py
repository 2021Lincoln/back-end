from funcionarios import Funcionarios

class Enfermeiro(Funcionarios):
    def __init__(self, matricula, nome, telefone, email, cpf, rg, coren):
        super().__init__(matricula, nome, telefone, email, cpf, rg, 'Enfermeiro')
        self.coren = coren

