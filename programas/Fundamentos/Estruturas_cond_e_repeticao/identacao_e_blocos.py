#atravez da indentacao o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.

def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("Valor sacado!")
        print("Retire seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
    saldo = 500
    saldo += valor
    print("Valor", valor, "depositado!")
    print("Novo saldo", saldo,)
    print("Obrigado por ser nosso cliente, tenha um bom dia!")


sacar(500) 
depositar(100)       