



class Pessoa: # Aqui está sendo criada a classe pessoa
    def __init__(self, nome, data_nascimento, sexo): #Aqui está sendo inicializada os atributos da classe pessoa O __init__ é um construtor que serve para dizer o que a classe pessoa vai ter.// o self é necessário ter para pegar os valores e referenciar os atributos
        self.nome = nome # Aqui são os atributos da classe pessoa
        self.data_nascimento = data_nascimento
        self.sexo = sexo

    def falar(self, mensagem): #Tudo o que está dentro da classe é considerado como ">>>>>MÉTODO<<<<<"
        print(f"{self.nome} diz: {mensagem}")



pessoa1 = Pessoa("José", "20/10/1995", "masculino")
pessoa2 = Pessoa("Lincoln", "30/08/1992", "masculino")
pessoa3 = Pessoa("Daniele", "26/01/1989", "feminino")


print("Nome:", pessoa1.nome, "Data de nascimento:", pessoa1.data_nascimento, "sexo", pessoa1.sexo)
print("Nome:", pessoa2.nome, "sexo:", pessoa2.sexo, "sexo", pessoa2.sexo)
print("Nome:", pessoa3.nome, "Data de nascimento:", pessoa3.data_nascimento, "sexo", pessoa3.sexo)


