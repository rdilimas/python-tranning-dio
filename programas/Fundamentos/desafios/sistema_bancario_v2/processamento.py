import textwrap

INF_VALOR_OPER_SAQUE = "Informe o valor do saque: "
INF_VALOR_OPER_DEPOS = "Informe o valor do depósito: "

OPER_FALHOU          = "Operação falhou!"
VLR_INF_INVALID      = "O valor informado é inválido."
NUM_MAX_SAQUE_EXEDID = "Número máximo de saques excedido."
SALDO_INSUFICIENTE   = "Você não tem saldo suficiente."
SAQUE_EXED_LIMIT_DIA = "O valor do saque excede o limite."
INFORME_O_CPF        = "Informe o CPF (somente número): "
INFORME_NOME_COMPLETO= "Informe o nome completo: "
INFORME_DT_NASCIMENTO= "Informe a data de nascimento (dd-mm-aaaa): "
INFORME_O_ENDERECO   = "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
CLIENTE_JA_CADASTRADO= "\n### Já existe cliente com esse CPF! ###"
CONTA_CRIADA_SUCESSO = "\n=== Conta criada com sucesso! ==="
CLIENTE_CRIADO_SUCESS= "=== Cliente criado com sucesso! ==="
CLIENTE_NAO_CADASTRAD= "\### Usuário não encontrado, fluxo de criação de conta encerrado! ###"




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


def criar_cliente(clientes):
    cpf = input(INFORME_O_CPF)
    usuario = filtrar_usuario(cpf, clientes)

    if usuario:
        print(CLIENTE_JA_CADASTRADO)
        return

    nome = input(INFORME_NOME_COMPLETO)
    data_nascimento = input(INFORME_DT_NASCIMENTO)
    endereco = input(INFORME_O_ENDERECO)

    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(CLIENTE_CRIADO_SUCESS)


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None    


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input(INFORME_O_CPF)
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(CONTA_CRIADA_SUCESSO)
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print(CLIENTE_NAO_CADASTRAD)

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))    

