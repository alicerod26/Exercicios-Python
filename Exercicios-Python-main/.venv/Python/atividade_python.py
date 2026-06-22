from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from sys import argv

class Voluntario(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Seja Voluntário")
        self.setGeometry(150, 50, 1000, 600)

        # Criar o layout horizontal principal
        self.layout_horizontal = QHBoxLayout()

        # ============ Trabalhando com a coluna da esquerda ================
        self.label_col_esquerda = QLabel()
        self.label_col_esquerda.setStyleSheet("QLabel{background-color:#ede7f6}")
        self.label_col_esquerda.setFixedWidth(500)

        # Criar o layout dos elementos da coluna da esquerda (layout vertical)
        self.layout_vert_col_esq = QVBoxLayout()

        # Criar a label para adicionar a imagem
        self.label_imagem = QLabel()
        self.label_imagem.setPixmap(QPixmap("imagem3.png"))
        self.label_imagem.setScaledContents(True)

        # Adicionar APENAS a imagem ao layout vertical esquerdo
        self.layout_vert_col_esq.addWidget(self.label_imagem)

        # Setar o layout vertical na label da coluna esquerda
        self.label_col_esquerda.setLayout(self.layout_vert_col_esq)


        # ============ Trabalhando com a coluna da direita ================
        self.label_col_direita = QLabel()
        self.label_col_direita.setStyleSheet("QLabel{background-color:#e1bee7}")

        # Criar o layout vertical da coluna da direita
        self.layout_vert_col_dir = QVBoxLayout()

        self.label_seja_voluntario = QLabel("Seja Voluntário")
        self.label_seja_voluntario.setStyleSheet("QLabel{font-weight:bold;font-size:24pt;font-family: 'Segoe UI';color:#673ab7; margin-top: 10px;}")
        self.label_seja_voluntario.setAlignment(Qt.AlignmentFlag.AlignCenter) # <--- Centraliza o texto

        # Criar e centralizar a label de subtítulo
        self.label_subtitulo = QLabel("Ajude um amigo a encontrar um lar")
        self.label_subtitulo.setStyleSheet("QLabel{font-size:14pt;font-family: 'Segoe UI';color:#673ab7; margin-bottom: 20px;}")
        self.label_subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter) # <--- Centraliza o texto

        # Criar a label e o edit do Nome
        self.label_seu_nome = QLabel("Seu Nome")
        self.label_seu_nome.setStyleSheet("QLabel{font-weight:bold;font-size:15pt;font-family: 'Segoe UI';color:#ba68c8}")
        self.edit_seu_nome = QLineEdit()
        self.edit_seu_nome.setStyleSheet("QLineEdit{border: 2px solid #ba68c8; font-weight:bold;font-size:15pt;font-family: 'Segoe UI';color:#ba68c8; background-color: #ffffff}")
        
        # Criar a label e o edit do E-mail
        self.label_seu_email = QLabel("Seu E-mail")
        self.label_seu_email.setStyleSheet("QLabel{font-weight:bold;font-size:15pt;font-family: 'Segoe UI';color:#ba68c8}")
        self.edit_seu_email = QLineEdit()
        self.edit_seu_email.setStyleSheet("QLineEdit{border: 2px solid #ba68c8; font-weight:bold;font-size:15pt;font-family: 'Segoe UI';color:#ba68c8; background-color: #ffffff}")
        
        # Criar a label e o edit da Senha
        self.label_sua_senha = QLabel("Sua Senha")
        self.label_sua_senha.setStyleSheet("QLabel{font-weight:bold;font-size:15pt;font-family: 'Segoe UI';color:#ba68c8}")
        self.edit_sua_senha = QLineEdit()
        self.edit_sua_senha.setEchoMode(QLineEdit.EchoMode.Password) 
        self.edit_sua_senha.setStyleSheet("QLineEdit{border: 2px solid #ba68c8; font-weight:bold;font-size:15pt;font-family: 'Segoe UI';color:#ba68c8; background-color: #ffffff}")

        # Criar o Botão Cadastrar
        self.botao_cadastrar = QPushButton("Cadastrar")
        self.botao_cadastrar.setStyleSheet("""QPushButton {background-color: #ba68c8; font-weight: bold;font-size: 15pt;font-family: 'Segoe UI';color: #ffffff;border-radius: 5px;padding: 10px;margin-top: 10px;}""")
        

        # Adicionar os controles ao layout da direita (Título inserido primeiro)
        self.layout_vert_col_dir.addWidget(self.label_seja_voluntario) 
        self.layout_vert_col_dir.addWidget(self.label_subtitulo)
        
        self.layout_vert_col_dir.addWidget(self.label_seu_nome)
        self.layout_vert_col_dir.addWidget(self.edit_seu_nome)
        
        self.layout_vert_col_dir.addWidget(self.label_seu_email)
        self.layout_vert_col_dir.addWidget(self.edit_seu_email)
        
        self.layout_vert_col_dir.addWidget(self.label_sua_senha)
        self.layout_vert_col_dir.addWidget(self.edit_sua_senha)
        
        self.layout_vert_col_dir.addWidget(self.botao_cadastrar)
        

        # Setar o layout vertical na label da coluna direita
        self.label_col_direita.setLayout(self.layout_vert_col_dir)

        # ============ Juntando tudo ================
        self.layout_horizontal.addWidget(self.label_col_esquerda)
        self.layout_horizontal.addWidget(self.label_col_direita)
        self.setLayout(self.layout_horizontal)


app = QApplication(argv)
janela = Voluntario()
janela.show()
app.exec()