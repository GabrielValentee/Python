import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MinhaJanela(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minha primeira janela")
        self.setGeometry(200, 200, 300, 200)  # x, y, largura, altura
        
        # Criar botões
        self.botao = QPushButton("Clique aqui")
        self.botao2 = QPushButton("Clique novamente")
        
        # Layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.botao)
        layout.addWidget(self.botao2)
        
        # Definir layout da janela
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)    # Inicializar a aplicação
    janela = MinhaJanela()          # Criar uma instância da janela
    janela.show()                   # Exibir a janela
    sys.exit(app.exec())            # Manter a aplicação em loop
