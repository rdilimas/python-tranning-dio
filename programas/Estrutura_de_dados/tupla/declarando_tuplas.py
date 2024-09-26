frutas = (
    "laranja",
    "pera",
    "uva",
)

print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)

frutas = (
    "laranja",
    "pera",
    "uva",
)

#é uma tupla?
print("frutas é uma tupla? ", isinstance(frutas, tuple))


#tuplas de um unico argumento precisa ser encerrado com "," para ajudar o compilador a entender que é um tupla.

carros = ("gol",) 
print("carros é uma tupla? ", isinstance(carros, tuple))

carros = ("gol") 
print("carros é uma tupla? ", isinstance(carros, tuple))