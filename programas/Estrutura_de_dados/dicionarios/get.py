contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

#Acessando direto pode dar erro quando não encontra a chave
# contatos["chave"]  # KeyError

#com o metodo get, caso não encontre a chave retorna None por padrão
resultado = contatos.get("chave")  # None
print(resultado)

#poder ser definidos outros valores de retorno para chave nao encontrada
resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)

carro = {"marca": "Fiat", "modelo": "palio", "placa": "ABD-9826"}
print("CArro", carro.get("motor"))