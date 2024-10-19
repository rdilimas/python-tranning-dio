def filtrar_visuais(lista_visuais):
    # Converter a string de entrada em uma lista
    visuais = lista_visuais.split(", ")
    
    # TODO: Normalize e remova duplicatas usando um conjunto
    #Removendo duplicados transformando a lista em conjunto
    for ind ,item in enumerate(visuais):
        visuais[ind] = item.title()
        
    conjunto_visuais = set(visuais) 
    
    # TODO: Converta o conjunto de volta para uma lista ordenada:
    lista_final = [] 
    lista_final = list(conjunto_visuais)
    lista_final.sort()
    
    # Unir a lista em uma string, separada por vírgulas
    return ", ".join(lista_final)

# Capturar a entrada do usuário
entrada_usuario = input()

# Processar a entrada e obter a saída
saida = filtrar_visuais(entrada_usuario)
print(saida)