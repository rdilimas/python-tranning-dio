

linguagens = ["python", "js", "c", "java", "csharp"]

#retorna a posição, dado um argumento a ser buscado na lista.
print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0

##Trecho de outra aula, percorrendo listas
for indice, linguagem in enumerate(linguagens):
    print(f"Posição {indice}.: {linguagem}")