conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

#Retorna o valor que tem no conjunto a e não tem no b
resultado = conjunto_a.difference(conjunto_b)
print(resultado)

#Retorna o valor que tem no conjunto ab e não tem no a
resultado = conjunto_b.difference(conjunto_a)
print(resultado)