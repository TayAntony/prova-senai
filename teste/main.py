import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PyQt5.uic import loadUi 

class MinhaJanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Minha Janela Principal')
        self.setGeometry(100, 100, 800, 600)

        # Carregue o arquivo .ui usando a função loadUi
        loadUi('teste_senai.ui', self)  # Substitua 'sua_janela.ui' pelo caminho correto

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela_principal = MinhaJanelaPrincipal()
    janela_principal.show()
    sys.exit(app.exec_())