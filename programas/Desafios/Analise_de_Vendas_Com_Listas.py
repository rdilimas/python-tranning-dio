def analise_vendas(vendas):
    # TODO: Calcule o total de vendas e realize a média mensal:
    tamanho_lista = len(vendas)
    total_vendas = 0
    for carro in vendas:
        total_vendas += carro
 
    media_vendas = total_vendas / tamanho_lista
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de inteiros:
    entrada_list = [] 
    entrada_list = entrada.split(',')
    vendas = [int(i) for i in entrada_list]
    
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))