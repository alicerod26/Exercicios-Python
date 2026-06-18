def acrescimo(preco:float,taxa:float):
    """ A função acréscimo realiza o cálculo de aumento
    do valor do preço do produto de acordo com a taxa

    Args:
        preco(float): Passe o preço do produto
        taxa(float): Passe a taxa do acréscimo somente número

    Returs:
        float: Retorna o preço do produto com o valor de acréscimo
    """
    return preco * (1+(taxa / 100))

rs = acrescimo(3580.20,8.6)
print(f"O valor final do produto é {rs}")