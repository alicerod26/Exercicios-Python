# Vammos uma variável chamada nome para guardar o nome do cliente. Utilizaremos tambem o comando input(in -> dentro | put -> por em algum lugar)
nome = input("Digite o seu nome: ")
print("Olá, Sr(a)."+nome)
print(f"Olá, Sr(a). {nome}")
# O operador +(mais) foi utilizado para concatenar(juntar) o texto entre aspas("") com a variável nome

print("Olá, Sr(a)."+nome+" . Seja bem vindo")
# Abaixo, usamos o comando print com a letra f(format) para inserir uma variável no meio de uma string. A variável foi inserida com chaves ({})
# está tecnica é chamada de interpolação
print(f"Olá, Sr(a). {nome}. Seja bem vindo")
