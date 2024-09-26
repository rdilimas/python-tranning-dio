conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

#retorna verdadeiro se todos os valores dos dois conjuntos são diferente
resultado = conjunto_a.isdisjoint(conjunto_b)  # True
print(resultado)

#retorna false, caso haja algum valor igual entre os dois conjuntos
resultado = conjunto_a.isdisjoint(conjunto_c)  # False
print(resultado)