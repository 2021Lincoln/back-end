from medico import Medico
from enfermeiro import Enfermeiro



cadastro = []

while True:
    tipo = input("Digite qual seu cargo M = Medico(a), E = Enfermeiro(a) ou S para sair: ")

    if tipo.upper() == 'S':
        break

    matricula = int(input("Digite a matricula o funcionario: "))
    nome = input("Digite a nome o funcionario: ")
    telefone = input("Digite o telefone do funcionario: ")
    email = input("Digite o email do funcionario: ")
    cpf = input("Digite o cpf do funcionario: ")
    rg = input("Digite o rg do funcionario: ")
    
    if tipo.upper() == 'M':
        crm = input("Digite o crm do funcionario: ")
        especialidade = input("Digite o especialidade do funcionario: ")
        horarios = input("Digite os horarios do funcionario: ")
        funcionario = Medico(matricula, nome, telefone, email, cpf, rg, crm, especialidade, horarios)
    elif tipo.upper() == 'E':
        coren = input("Digite o coren do enfermeiro: ")
        funcionario = Enfermeiro(matricula, nome, telefone, email, cpf, rg, coren)
    else:
        print("tipo invalido. Por favor, digite M para Medico(a), E para Enfermeiro(a) ou S para sair.")


    cadastro.append(funcionario)

print("Lista de Funcionarios: ")

for funcionario in cadastro:
    if(funcionario.cargo == 'Médico'):
        print(funcionario.nome, '-', funcionario.cargo, '-', funcionario.crm)
    
    if(funcionario.cargo == 'Enfermeiro'):
        print(funcionario.nome, funcionario.cargo, '-', funcionario.coren)


while True:
    resp = input("Deseja visualizar o horário dos médicos? Digite S para sim ou N para não: ")

    if resp.upper() == 'S':
        for funcionario in cadastro:
            if funcionario.cargo == "Médico":
                funcionario.informacao()

        break
    else:
        break


