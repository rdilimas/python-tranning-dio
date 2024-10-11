import textwrap
from abc import ABC, abstractclassmethod, abstractmethod, abstractproperty
from datetime import datetime

#Editar e entregar o projeto no desafio de POO  

INF_CPF_CLIENTE         = "Informe o CPF do cliente: "
OPERACAO_FALHOU         = "\n@@@ Operação falhou!"
DEP_REALIZADA_SUCESSO   = "\n=== Déposito realizado com sucesso! ===" 
SAQUE_REALIZADO_SUCESSO = "\n=== Saque realizado com sucesso! ==="
VLR_INFOR_IVALIDO       = " O valor informado é inválido. @@@"
OPERACAO_INVALIDA       = "\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@"
SAQUE_ADICIONAL         = """\n
                          =========== SAQUE ADICIONAL ===========
                          Taxa por saque adicional R$ 4,50
                          Deseja contratar saque adicional?
                         [s] - Sim
                         [n] - Não   
                         => """
EXCED_NUM_TRANS_DIA     = "\n@@@ Você excedeu o número de transações permitidas para hoje! @@@"           
SALDO_INSUFICIENTE      = " Você não tem saldo suficiente. @@@"
VLR_SAQUE_EXCEDE_LIMIT  = " O valor do saque excede o limite. @@@"
MAX_SAQUE_EXCEDIDO      = " Número máximo de saques excedido. @@@"
CLIE_NAO_PUSSUI_CONTA   = "\n@@@ Cliente não possui conta! @@@"
INFORME_VLR_DEPOSITO    = "Informe o valor do depósito: "
CLIE_NAO_ENCONTRADO     = "\n@@@ Cliente não encontrado! @@@"
NAO_FORAM_REALIZADAS_MOV= "Não foram realizadas movimentações"
INFO_VLR_SAQUE          = "Informe o valor do saque: "
INFO_O_CPF_NUMERICO     = "Informe o CPF (somente número): "
JA_EXISTE_CLIENTE       = "\n@@@ Já existe cliente com esse CPF! @@@"
INFORME_NOME_COMPLETO   = "Informe o nome completo: "
INFORME_DT_NASCIMENTO   = "Informe a data de nascimento (dd-mm-aaaa): "
INFORME_ENDERECO        = "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
CLIENTE_CRIADO_SUCESSO  = "\n=== Cliente criado com sucesso! ==="
CONTA_CRIADO_SUCESSO    = "\n=== Conta criada com sucesso! ==="
CLIE_NAO_ENCONTRADO_2   = "\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@"

        
class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self._index]
            return f"""\
            Agência:\t{conta.agencia}
            Número.:\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo..:\tR$ {conta.saldo:.2f}
        """
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        self.indice_conta = 0

    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= 5:
            print(EXCED_NUM_TRANS_DIA)
            return
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print(OPERACAO_FALHOU, SALDO_INSUFICIENTE)

        elif valor > 0:
            self._saldo -= valor
            print(SAQUE_REALIZADO_SUCESSO)
            return True

        else:
            print(OPERACAO_FALHOU, VLR_INFOR_IVALIDO)

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(DEP_REALIZADA_SUCESSO)
        else:
            print(OPERACAO_FALHOU, VLR_INFOR_IVALIDO)
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    @classmethod
    def nova_conta(cls, cliente, numero, limite, limite_saques):
        return cls(numero, cliente, limite, limite_saques)

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print(OPERACAO_FALHOU, VLR_SAQUE_EXCEDE_LIMIT)

        elif excedeu_saques:
            print(OPERACAO_FALHOU, MAX_SAQUE_EXCEDIDO)
            aceita_taxa_saque = Saque.saque_adicional().lower()
            if aceita_taxa_saque == 's':
               taxa_saque_adicional = 4.50
               valor += taxa_saque_adicional
               return super().sacar(valor)

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C....:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao

    def transacoes_do_dia(self):
        data_atual = datetime.now().date()
        transacoes = []
        for transacao in self._transacoes:
            data_transacao = datetime.strptime(transacao["data"], "%d-%m-%Y %H:%M:%S").date()
            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

    def saque_adicional():
     return input(textwrap.dedent(SAQUE_ADICIONAL))            


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"{datetime.now()}: {func.__name__.upper()}")
        return resultado

    return envelope


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


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print(CLIE_NAO_PUSSUI_CONTA)
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]


@log_transacao
def depositar(clientes):
    cpf = input(INF_CPF_CLIENTE)
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(CLIE_NAO_ENCONTRADO)
        return

    valor = float(input(INFORME_VLR_DEPOSITO))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


@log_transacao
def sacar(clientes):
    cpf = input(INF_CPF_CLIENTE)
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(CLIE_NAO_ENCONTRADO)
        return

    valor = float(input(INFO_VLR_SAQUE))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


@log_transacao
def exibir_extrato(clientes):
    cpf = input(INF_CPF_CLIENTE)
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(CLIE_NAO_ENCONTRADO)
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    extrato = ""
    tem_transacao = False
    for transacao in conta.historico.gerar_relatorio():
        tem_transacao = True
        extrato += f'\n{transacao["tipo"]}:\n\tR$ {transacao["valor"]:.2f}'

    if not tem_transacao:
        extrato = NAO_FORAM_REALIZADAS_MOV

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


@log_transacao
def criar_cliente(clientes):
    cpf = input(INFO_O_CPF_NUMERICO)
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print(JA_EXISTE_CLIENTE)
        return

    
    nome = input(INFORME_NOME_COMPLETO)
    data_nascimento = input(INFORME_DT_NASCIMENTO)
    endereco = input(INFORME_ENDERECO)

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print(CLIENTE_CRIADO_SUCESSO)


@log_transacao
def criar_conta(numero_conta, clientes, contas):
    cpf = input(INF_CPF_CLIENTE)
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(CLIE_NAO_ENCONTRADO_2)
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta, limite=500, limite_saques=3)
    contas.append(conta)
    cliente.contas.append(conta)

    print(CONTA_CRIADO_SUCESSO)


def listar_contas(contas):
    for conta in ContasIterador(contas):
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu().lower()
        
        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print(OPERACAO_INVALIDA)


main()