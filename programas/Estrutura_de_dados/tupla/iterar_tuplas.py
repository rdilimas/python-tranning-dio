carros = (
    "gol",
    "celta",
    "palio",
)

for carro in carros:
    print(carro)

#Com enumerate para termos acesso ao indice
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")