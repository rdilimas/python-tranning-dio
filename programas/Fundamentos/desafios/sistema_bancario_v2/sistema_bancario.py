import processamento
import textwrap

OPER_INVALIDA        = "Operação inválida, por favor selecione novamente a operação desejada."

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def main():

    #constantes
    LIMITE_SAQUES = 3
    AGENCIA   = 1

    #variaveis
    saldo   = 0
    extrato = ""
    limite = 500
    numero_saques = 0
    clientes = []
    contas = []



    while True:
        opcao = menu()
        if opcao == "d":
            saldo, extrato = processamento.depositar(saldo, 
                                                     extrato)
       
        elif opcao == "s":
            saldo, extrato, numero_saques= processamento.sacar(saldo=saldo, 
                                                 extrato=extrato, 
                                                 limite=limite, 
                                                 numero_saques=numero_saques, 
                                                 limite_saques=LIMITE_SAQUES)
  
        elif opcao == "e":
             processamento.imprimir_extrato(saldo, 
                                            extrato=extrato)  
             
        elif opcao == "nu":
            processamento.criar_cliente(clientes)   

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = processamento.criar_conta(AGENCIA, numero_conta, clientes)

            if conta:
                contas.append(conta)  

        elif opcao == "lc":
            processamento.listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print(OPER_INVALIDA)


main()


       