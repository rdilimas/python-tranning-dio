import time

entrada = "Webcam, Webcam, Headset, Monitor, Headset, Headset"

print("Entrada.............: ", entrada)

entrada_list = []
entrada_list = entrada.split(',')

print()
print("Quebrados em Lista..: ", entrada_list)
    
#split() não funciona setando na propria lista, deve ser aplicado lendo de uma lista e gravando em outra
produtos = [produto.strip() for produto in entrada_list]
print()
print("Removidos os espacos: ", produtos)

ind = 0

for prod in produtos:
    ind = ind + 1
    print("Produto: ", prod, "| Posição: ", ind)
    time.sleep(1)
