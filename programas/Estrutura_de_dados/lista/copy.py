

lista = [1, "Python", [40, 30, 20]]


lista_2 = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

lista_2.append("Novo item")

#Depois de copiada são listas independentes
print(lista_2)