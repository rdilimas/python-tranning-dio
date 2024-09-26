numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(0))  # 0
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

print("")
letras = {"a", "b", "c", "d"}

print(letras) 

#retorna Nome porque o metodo remove não tem retorno
#Erro, se tentar remover um valor que não exista
print(letras.remove("a"))  # 0
letras.remove("b") # 0
print(letras)