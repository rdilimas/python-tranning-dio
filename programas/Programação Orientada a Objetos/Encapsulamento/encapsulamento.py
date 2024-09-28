#Metodos e atributos privados iniciam com _
#_metodo() -- Não fazer chamadas a esse tipo de metodo em classe externa
#_variável -- Não acessar diretamente variáveis encapsuladas fora da classe de definição
#

class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def mostrar_saldo(self):
        # ...
        return self._saldo


conta = Conta("0001", 100)
conta.depositar(100)


print(conta.nro_agencia)

print(conta.mostrar_saldo())