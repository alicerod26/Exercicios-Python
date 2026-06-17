from PyQt6.QtWidgets import QApplication, QWidget,QLabel,QLineEdit,QTableWidget, QVBoxLayout,QHBoxLayout
from PyQt6.QtGui import QPixmap
from sys import argv
 
class Caixa(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Caixa da Padaria")
        self.setGeometry(150,50,1600,900)
 
        # Criar o layout horizontal
        self.layout_horizontal = QHBoxLayout()
        # Vamos criar as duas colunas: Esquerda e Direita
        self.label_col_esquerda = QLabel()
        # Alterar a cor de fundo da label esquerda
        self.label_col_esquerda.setStyleSheet("QLabel{background-color:#ef9a9a}")
        # Largura fixa
        self.label_col_esquerda.setFixedWidth(800)
 
        # Criar o layout dos elementos da coluna da esquerda. Este layout é vertical
        self.layout_vert_col_esq = QVBoxLayout()
 
        # Vamos criar uma label para adicionar o logo da padaria
        self.label_logo = QLabel()
        # Vamos setar o Pixmap a label para carregar a imagem
        self.label_logo.setPixmap(QPixmap("logo6.png"))
        # Ajustar a imagem a label
        self.label_logo.setScaledContents(True)
 
        # Criar a label do código de produto
        self.label_cod_produto = QLabel("Código do Produto")
        self.label_cod_produto.setStyleSheet("QLabel{font-weight:bold;font-size:15pt;font-family: 'Segoe UI';color:#ffffff}")
        self.edit_cod_produto = QLineEdit()
        self.edit_cod_produto.setStyleSheet("QLineEdit{border: 2px solid #4db6ac; font-weight:bold;font-size:15pt;font-family: 'Segoe UI';color:#4db6ac}")
 
       
        # Criar a label e o edit do nome de produto
        self.label_nome_produto = QLabel("Nome do Produto")
        self.label_nome_produto.setStyleSheet("QLabel{font-weight:bold;font-size:15pt;font-family: 'Segoe UI';color:#ffffff}")
        self.edit_nome_produto = QLineEdit()
        self.edit_nome_produto.setStyleSheet("QLineEdit{border: 2px solid #4db6ac;font-weight:bold;font-size:15pt;font-family: 'Segoe UI';color:#4db6ac}")
 
        # Criar a label e o edit do descricao de produto
        self.label_descricao_produto = QLabel("Descrição do Produto")
        self.label_descricao_produto.setStyleSheet("QLabel{font-weight:bold;font-size:15pt;font-family: 'Segoe UI';color:#ffffff}")
        self.edit_descricao_produto = QLineEdit()
        self.edit_descricao_produto.setStyleSheet("QLineEdit{border: 2px solid #4db6ac;font-weight:bold;font-size:15pt;font-family: 'Segoe UI';color:#4db6ac}")
        # Tamanho da caixa de descrição
        self.edit_descricao_produto.setFixedHeight(100)
 
        # Criar a label e o edit do quantidade de produto
        self.label_quantidade_produto = QLabel("Quantidade do Produto")
        self.label_quantidade_produto.setStyleSheet("QLabel{font-weight:bold;font-size:15pt;font-family: 'Segoe UI';color:#ffffff}")
        self.edit_quantidade_produto = QLineEdit()
        self.edit_quantidade_produto.setStyleSheet("QLineEdit{border: 2px solid #4db6ac;font-weight:bold;font-size:15pt;font-family: 'Segoe UI';color:#4db6ac}")
 
        # Criar a label e o edit do preço unitário de produto
        self.label_preco_produto = QLabel("Preço Unitário do Produto")
        self.label_preco_produto.setStyleSheet("QLabel{font-weight:bold;font-size:15pt;font-family: 'Segoe UI';color:#ffffff}")
        self.edit_preco_produto = QLineEdit()
        self.edit_preco_produto.setStyleSheet("QLineEdit{border: 2px solid #4db6ac;font-weight:bold;font-size:15pt;font-family: 'Segoe UI';color:#4db6ac}")
 
        # Criar a label e o edit do sub total de produto
        self.label_sub_total_produto = QLabel("Subtotal do Produto")
        self.label_sub_total_produto.setStyleSheet("QLabel{font-weight:bold;font-size:15pt;font-family: 'Segoe UI';color:#ffffff}")
        self.edit_sub_total_produto = QLineEdit("Tecle F3 para calcular o subtotal")
        self.edit_sub_total_produto.setStyleSheet("QLineEdit{border: 2px solid #4db6ac;font-weight:bold;font-size:15pt;font-family: 'Segoe UI'; color:#4db6ac}")
        # Bloquear a edição do subtotal
        self.edit_sub_total_produto.setEnabled(False)
 
       
        # Adicionar o logo ao layout vertical
        self.layout_vert_col_esq.addWidget(self.label_logo)
 
        # Adicionar o código do produto
        self.layout_vert_col_esq.addWidget(self.label_cod_produto)
        self.layout_vert_col_esq.addWidget(self.edit_cod_produto)
 
        # Adicionar o nome do produto
        self.layout_vert_col_esq.addWidget(self.label_nome_produto)
        self.layout_vert_col_esq.addWidget(self.edit_nome_produto)
 
        # Adicionar o descrição do produto
        self.layout_vert_col_esq.addWidget(self.label_descricao_produto)
        self.layout_vert_col_esq.addWidget(self.edit_descricao_produto)
 
        # Adicionar o quantidade do produto
        self.layout_vert_col_esq.addWidget(self.label_quantidade_produto)
        self.layout_vert_col_esq.addWidget(self.edit_quantidade_produto)
 
        # Adicionar o preço unitário do produto
        self.layout_vert_col_esq.addWidget(self.label_preco_produto)
        self.layout_vert_col_esq.addWidget(self.edit_preco_produto)
 
        # Adicionar o sub total do produto
        self.layout_vert_col_esq.addWidget(self.label_sub_total_produto)
        self.layout_vert_col_esq.addWidget(self.edit_sub_total_produto)
 
        # Setar o layout vertical a label coluna esquerda
        self.label_col_esquerda.setLayout(self.layout_vert_col_esq)
       
       
       
       # ============ Trabalahndo com a coluna da direita ================
       
        self.label_col_direita = QLabel()
        self.label_col_direita.setStyleSheet("QLabel{background-color:#80cbc4}")
       
       # Criar o layout vertical da colona da diereita para os elementos
       # QTablewidget, Qlabel, QlineEdit

        self.layout_vert_col_dir = QVBoxLayout()

        self.tabela_produtos = QTableWidget()
        # Criar os itens do cabeçalho da tabela
        cabecalho = ["Cód.Produto" , "Produto" , "Quantidade" , "Preço" , "Sub total"]
        # Definir a quantidade de colunas da nossa tabela
        self.tabela_produtos.setColumnCount(5)
        # Adicionar o cabeçalho a tabela
        self.tabela_produtos.setHorizontalHeaderLabels(cabecalho)
        



        self.label_total_pagar = QLabel("Total a Pagar")
        self.label_total_pagar.setStyleSheet("QLabel{font-weight:bold;font-size:15pt;font-family: 'Segoe UI'; color:#00695c}")

        self.edit_total_pagar = QLineEdit("0,00")
        self.edit_total_pagar.setStyleSheet("QLineEdit{border: 2px solid #4db6ac;font-weight:bold;font-size:15pt;font-family: 'Segoe UI'; color:#e57373}")

        # Adicionar os controles ao layout vertical da coluna da direita
        self.layout_vert_col_dir.addWidget(self.tabela_produtos)
        self.layout_vert_col_dir.addWidget(self.label_total_pagar)
        self.layout_vert_col_dir.addWidget(self.edit_total_pagar)

        # Setar o layout vertical da coluna da direita na coluna da direita
        self.label_col_direita.setLayout(self.layout_vert_col_dir)
 
 
 
 
        # Adicionar as colunas esquerda e direita ao layout horizontal
        self.layout_horizontal.addWidget(self.label_col_esquerda)
        self.layout_horizontal.addWidget(self.label_col_direita)
 
        # Setar o layout horizontal a nossa janela
        self.setLayout(self.layout_horizontal)
 
 
app = QApplication(argv)
janela = Caixa()
janela.show()
app.exec()
  
 
 