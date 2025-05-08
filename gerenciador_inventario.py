class Inventario:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"{item} adicionado ao inventário.")

    def listar_itens(self):
        print("Itens no inventário")
        if not self.itens:
            print("O inventário está vazio.")
        else:
            for i, item in enumerate(self.itens):
                print(f"{i +1}.{item}")

meu_inventario = Inventario()

meu_inventario.adicionar_item("Espada Longa")
meu_inventario.adicionar_item("Escudo de Madeira")
meu_inventario.adicionar_item("Poção de cura")
meu_inventario.adicionar_item("Flechas (x20)")
meu_inventario.adicionar_item("Peitoral de diamante")
meu_inventario.adicionar_item("batata(x19)")
meu_inventario.adicionar_item("Ender Pearl (x8)")

meu_inventario.listar_itens()