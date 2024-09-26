#Métodos úteis
curso = "pYtHoN"

print(curso.upper())

print(curso.lower())

print(curso.title())


curso = "     Python     "

print(curso.strip() + ".")

print(curso.lstrip()+ ".")

print(curso.rstrip()+ ".")


curso = "Python"

print(curso.center(10 , "#"))

print(".".join(curso))

print()
menu = "Python"

#Resultado aproximado, porem precisa ainda tratar a ultima letra para nao imprimir ponto após ela
for letra in menu:
    print(letra, end=".")

