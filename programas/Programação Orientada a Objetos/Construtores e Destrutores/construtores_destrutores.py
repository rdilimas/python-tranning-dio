class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    #não é tão utilizado porque o python tem um gerenciamento automatico do coletor de lixo
    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("auau")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


c = Cachorro("Chappie", "amarelo")
c.falar()

print("Ola mundo")


#força a destruição da instancia 
del c

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

# criar_cachorro()