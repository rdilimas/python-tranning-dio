
numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

print("numeros é um conjunto: ", isinstance(numeros, set))

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

print("Letras é um conjunto: ", isinstance(letras, set))

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

print("Carro é um conjunto: ", isinstance(carros, set))

#pode ser declarado também com chaves

carros = {"palio", "gol", "celta", "palio"}
print(carros)

print("Carro é um conjunto: ", isinstance(carros, set))
