def somar_reais(lista):
    """
    Somar os elementos de uma lista de reais. Serão somados apenas os números que são maiores do que o número na próxima posição.

    Argumentos: lista: uma lista de números reais
    
    Retorno: soma dos elementos que atendem à condição proposta
    """
    soma = 0

    for item in range(len(lista)-1):
        if lista[item] > lista[item + 1]:
            soma += lista[item]

    return soma

soma = somar_reais([1.5, 2, 7, 5, 1])
print(soma)

def somar_reais2(lista):
    return sum(lista[item] for item in range(len(lista) - 1) if lista[item] > lista[item + 1])

soma = somar_reais2([1.5, 2, 7, 5, 1])
print(soma)