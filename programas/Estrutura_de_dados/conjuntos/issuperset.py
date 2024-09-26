conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

#retorna falso, caso os valores de a não contenham b
resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado)

#retorna verdadeiro, caso todos os valores de a estejam em b
resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado)