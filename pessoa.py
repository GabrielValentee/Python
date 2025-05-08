class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        print(f"Objeto pessoa {self.nome} e eu sou {self.profissao}.")

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu sou {self.profissao}.")

    def envelhecer(self):
        self.idade += 1
        print(f"{self.nome} agora tem {self.idade} anos.")

pessoa1 = Pessoa("Ana Clara", 30, "Programadora")
pessoa2 = Pessoa("Paulo", 28, "Desenvolvedor Full Stack")

pessoa1.apresentar()
pessoa2.apresentar()

pessoa1.envelhecer()
pessoa2.envelhecer()

pessoa1.apresentar()
pessoa2.apresentar()

pessoa1.envelhecer()
pessoa2.envelhecer()
