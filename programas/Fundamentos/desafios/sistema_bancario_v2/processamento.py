INF_VALOR_OPER_SAQUE = "Informe o valor do saque: "
INF_VALOR_OPER_DEPOS = "Informe o valor do depósito: "

OPER_FALHOU          = "Operação falhou!"
VLR_INF_INVALID      = "O valor informado é inválido."
NUM_MAX_SAQUE_EXEDID = "Número máximo de saques excedido."
SALDO_INSUFICIENTE   = "Você não tem saldo suficiente."
SAQUE_EXED_LIMIT_DIA = "O valor do saque excede o limite."


#recebe os valor por posição : antes da barra
#                por keywargs: depois do *   
def imprimir_extrato(saldo, /, *, extrato):
    print(" EXTRATO ".center(41 , "="))
    print("Não foram realizadas movimentações." if not extrato else extrato )
    print(f"\nSaldo....: R$ {saldo:.2f}")
    print("==========================================")


#Passagem de dados por posição apenas, deve ser respeitada a ordem
def depositar(saldo, extrato, /):
    
    valor = float(input(INF_VALOR_OPER_DEPOS))
    if valor > 0:
       saldo += valor
       extrato += f"Depósito.: R$ {valor:.2f}\n"
    else:
       print(OPER_FALHOU,VLR_INF_INVALID)  

    return saldo, extrato   


#Passagem de parametro por KeyWargs CHAVE E VALOR
def sacar(*, saldo, extrato, limite, numero_saques, limite_saques):
     
     valor = float(input(INF_VALOR_OPER_SAQUE))

     excedeu_saldo = valor > saldo

     excedeu_limite = valor > limite

     excedeu_saques = numero_saques >= limite_saques
     
     if excedeu_saldo:
         print(OPER_FALHOU,SALDO_INSUFICIENTE)

     elif excedeu_limite:
          print(OPER_FALHOU,SAQUE_EXED_LIMIT_DIA)

     elif excedeu_saques:
          print(OPER_FALHOU,NUM_MAX_SAQUE_EXEDID)

     elif valor > 0:
          saldo -= valor
          extrato += f"Saque....: R$ {valor:.2f}\n"
          numero_saques += 1

     else:
          print(OPER_FALHOU,VLR_INF_INVALID)

     return saldo, extrato, numero_saques

