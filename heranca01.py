class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar (self):
        print(f"Olá meu nome é {self.nome} e tenho {self.idade} anos.")

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.curso = curso

    def apresentar(self):
            print("Olá, meu nome é {self.nome}, tenho {self.idade}" \
            " anos e sou aluno do curso de {self.curso}, matrícula")

    def estudar(self):
            print(f"Olá meu nome é {self.nome}, tenho {self.idade} anos e sou aluno do curso de {self.curso}, matrícula {self.matricula} está estudando {self.curso}.")

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def apresentar(self):
        print(f"Olá meu nome é {self.nome}, tenho {self.idade} anos e sou professor de {self.disciplina}.")

    def dar_aula(self):
        print(f"{self.nome} está dando aula de {self.disciplina}")

aluno1 = Aluno("Joelma Lima", 45, "202505", "Programando com python")
professor1 = Professor("Mateus Almeida", 25, "Programando com python")

aluno1.apresentar()
professor1.apresentar()

aluno1.estudar()
professor1.dar_aula()

print(f"Nome de aluno: {aluno1.nome}, Matrícula: {aluno1.matricula}.")
