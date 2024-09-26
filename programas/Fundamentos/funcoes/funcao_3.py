
def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")



salvar_carro("Fiat", "Grand Siena", "2014", "ABC1234")


salvar_carro(**{"marca":"Fiat","modelo": "Grand Siena","ano": "2014", "placa": "ABC1234"})


def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()} : {valor}" for chave, valor in kwargs.items()]) 
    mensagem = f"{data_extenso} \n\n {texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema("Sexta-feira, 23 setembro de 2024", 
             
             #args pode receber uma lista          
             " Zen of Python", 
             "Beaultfull is better than ugly.", 
             "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
             "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
             "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
             "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
             #quando encontra uma entrada diferente, muda para o kwargs
             #que é chave e valor
             # * lista de argumentos
             # ** chave e valor
             autor="Tim Peters", 
             ano=1999)    