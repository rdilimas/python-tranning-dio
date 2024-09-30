class Passaro:
    def voar(self):
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")

#acessa o metodo do pai
class Aguia(Passaro):
    def voar(self):
        super().voar()  

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


# NOTE: exemplo ruim do uso de herança para "ganhar" o método voar
#Avião não pode ser herdeiro da classe Passaro
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")


def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
plano_voo(Aguia())