conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

#retorna verdadeiro se todos os valores do conjunto a estiver em b
resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado)

#retorna false, caso todos os valores de b não estejam em a
resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado)