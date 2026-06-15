from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import sys

class Janela2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minha Janela")
        #Largura, altura e posição da janela
        self.setGeometry(50,80,800,400)

app = QApplication(sys.argv)
tela = Janela2()
tela.show()
app.exec()


