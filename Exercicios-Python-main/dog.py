class Dog:
    def __init__ (self, nome, age):
        self.nome = nome
        self.age = age

    def sit(self):
        print(f"O {self.nome} sentou")

    def roll_over(self):
        print(f"O {self.nome} rolou")
        
meu_cachorro = Dog ("Zeus",5)
meu_cachorro.sit()
meu_cachorro.roll_over()
