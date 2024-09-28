class Bicicleta:

    #construtor
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    #metodo é igual a uma função, porém precisas estar dentro de uma classe e deve ter ao menos um argumento
    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

    
    def __str__(self):
    #   return f"{self.__class__.__name__}:" 
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)

#chama implicitamento o metodo __str__
print("Imprimindo o Obj", b2)

#duas formas equivalentes de chamar
b2.correr()
Bicicleta.correr(b2)


print(b2.cor)