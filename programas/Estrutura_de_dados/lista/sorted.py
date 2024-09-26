

linguagens = ["python", "js", "c", "java", "csharp"]

#Ordena pelo tamanho da string menor para o maior
print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]

#Ordena pelo tamanho da string maior para o menor
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]