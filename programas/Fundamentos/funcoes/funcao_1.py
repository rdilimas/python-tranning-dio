
def exibir_mensagem():
    print("Alá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anonimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()

exibir_mensagem_2("Robson")

#se não passar nome ele assumi o valor padrão definido na assinatura da funcao
exibir_mensagem_3()
exibir_mensagem_2("Robson")
