class Gato:
    def __init__(self,raca:str,cor:str,tipo_pelo:str,idade:int,nome:str):
        """
        Docstring for _init_
        
        :param self: Comando que faz ps atributos e métodos olharem para a classe 
        :param raca: Digite a raça do gato
        :type raca: str
        :param cor: Digite a cor do gato
        :type cor: str
        :param tipo_pelo: Digite o tipo de pelo (Sem pelo, Pelo longo, Pelo curto)
        :type tipo_pelo: str
        :param idade: Digite a idadedo gato com número inteiro
        :type idade: int
        :param name: Deigite o nome do gato
        :type name: str
        """
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.cor = cor
        self.tipo_pelo = tipo_pelo

    def miar(self):
        print(f"A {self.nome} miou")

meu_gato = Gato ("Angorá", "Branca", "Pelo longo", 7, "Lua")
meu_gato.miar()
