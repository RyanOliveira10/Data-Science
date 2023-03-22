# Conta Bancaria

class Conta_Bancaria:
    def __init__(self):
        self.nome = None
        self.numero_conta = None
        self.email = None
        self.endereco = None
        self.telefone = None
        self.manutencao_conta = None
        self._saldo = 0

    def depositar(self, valor):
        self.valor += valor
        return valor

    def _checar_saldo(self, valor):
        self._saldo += valor

    def obter_saldo(self):
        return self._saldo

    def sacar(self, valor):
        if self._checar_saldo(valor):
            self._saldo -= valor
            return True
        else:
            return False


class Cartao:
    def __init__(self):
        self.titular = None
        self.tipo_cartao = None
        self._senha = None
        self._senha_seguranca = None
        self.validade = None
        self.codigo = None
        self.numero_cartao
        pass

    def realizar_pagamento(valor):
        # codigo aqui
        return


class Conta_Corrente(Conta_Bancaria, Cartao):

    def __init__(self):
        self.manutencao_conta = 10
        self.tipo_cartao = ['credito', 'debito']
        self.titular = self.nome

    def solicitar_emprestimo(self, valor):
        if self.obter_saldo() >= 1000:
            return valor
        else:
            print("credito negado!")

        # polimorfismo metodo sacar
        # polimorfismo metodo depositar
        # polimorfismo metodo obter saldo
        return


class Conta_Poupanca(Conta_Bancaria, Cartao):
    def __init__(self):
        self.manutencao_conta = 0
        self.tipo_cartao = ['debito']

    # polimorfismo metodo sacar
    # polimorfismo metodo depositar
    # polimorfismo metodo obter saldo


class ContaPF(Conta_Corrente, Conta_Poupanca):
    def __init__(self):
        self.cpf = None

    # polimorfismo solicitar emprestimo


class ContaPJ(Conta_Corrente):
    def __init__(self):
        self.cnpj = None

    def sacar_emprestimo(self, valor):
        return valor <= 5000

    # polimorfismo solicitar emprestimo
