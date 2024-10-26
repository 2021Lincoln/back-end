



class Pessoa: # Aqui está sendo criada a classe pessoa
    def __init__(self, nome, data_nascimento, sexo): #Aqui está sendo inicializada os atributos da classe pessoa // o self é necessario ter para pegar os valores e referenciar os atributos
        self.nome = nome # Aqui são os atributos da classe pessoa
        self.data_nascimento = data_nascimento
        self.sexo = sexo

    def falar(self, mensagem):
        print(f"{self.nome} diz: {mensagem}")



pessoa1 = Pessoa("José", "20/10/1995", "masculino")
pessoa2 = Pessoa("Lincoln", "30/08/1992", "masculino")
pessoa3 = Pessoa("Daniele", "26/01/1989", "feminino")


print("Nome:", pessoa1.nome, "Data de nascimento:", pessoa1.data_nascimento)
print("Nome:", pessoa2.nome, "sexo:", pessoa2.sexo)
print("Nome:", pessoa3.nome, "Data de nascimento:", pessoa3.data_nascimento)
