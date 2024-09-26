
linguagens = ["python", "js", "c"]
print(linguagens)  # ["python", "js", "c"]



linguagens_2 = ["java", "csharp"]
#concatena duas listas
linguagens.extend(linguagens_2)
print(linguagens)  # ["python", "js", "c", "java", "csharp"]

#a lista adicionada não tem seu estado alterado.
print(linguagens_2)


print([n**2 if n > 6 else n for n in range(10) if n % 2 == 0])