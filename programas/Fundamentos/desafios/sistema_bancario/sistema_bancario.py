import processamento

OPER_INVALIDA        = "Operação inválida, por favor selecione novamente a operação desejada."

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

while True:
    opcao = input(menu)
    if opcao == "d":
        processamento.depositar()
       
    elif opcao == "s":
        processamento.sacar()
  
    elif opcao == "e":
         processamento.imprimir_extrato()  

    elif opcao == "q":
        break

    else:
        print(OPER_INVALIDA)


       