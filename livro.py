class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def detalhes(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas {self.paginas}")

    def eh_longo(self):
        return self.paginas > 300
    
livro1 = Livro("O senhor dos anéis", "J.R.R Tolkien", 1200)
livro2 = Livro("Crepúsculo", "Stephany Meyer", 100)

livro1.detalhes()
print(f"O livro 1 é longo? {livro1.eh_longo()}")

print("-" * 20)

livro2.detalhes()
print(f"O livro 2 é longo? {livro2.eh_longo()}")