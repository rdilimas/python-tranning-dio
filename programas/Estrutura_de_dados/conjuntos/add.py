sorteio = {1, 23}

sorteio.add(25)  # {1, 23, 25}
print(sorteio)

sorteio.add(42)  # {1, 23, 25, 42}
print(sorteio)

#tentar adicionar um valor que já exista, não da erro
#simplesmente, não adiciona, pela caracteristica de conjuntos não
#conter valores repetidos.
sorteio.add(25)  # {1, 23, 25, 42}
print(sorteio)