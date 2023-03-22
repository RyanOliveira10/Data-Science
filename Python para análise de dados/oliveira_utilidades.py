from datetime import datetime, timezone, timedelta


class Pessoa:
    def __init__(self):
        self.cpf = None
        self.nome = None
        self.endereco = None


class Funcionario(Pessoa):
    def __init__(self):
        self.matricula = None
        self.salario = None
        self.senha = None

    def bater_ponto(self):
        print("Ponto batido em "), Date_time_system.exibir_data_hora(self)
        pass

    def fazer_login(self):
        self.usuario = 'admin'
        self.senha = 'admin'

        u = input("\nDigite seu usuario: ")
        s = input("\nDigite sua senha: ")

        while True:
            def valida_login(usuario, senha):
                if usuario == self.usuario and senha == self.senha:
                    print("usuario logado!\n")
                    self.bater_ponto()
                else:
                    print("Usuario ou senha incorretos!")

            valida_login(usuario=u, senha=s)
    pass


class Cliente(Pessoa):
    def __init__(self):
        self.codigo = None
        self.data_cadastro = None

    def realizar_cadastro():

        pass

    def fazer_compra(self):

        pass

    def pagar_conta(self):

        pass


class Date_time_system:

    def __init__(self):
        self.data = None
        pass

    def exibir_data_hora(self):
        data_hora_atual = datetime.now()
        diferenca = timedelta(hours=-3)
        fuso_horario = timezone(diferenca)
        data_hora_atual.astimezone(fuso_horario)
        data_hora = data_hora_atual.strftime("%d/%m/%Y %H:%M")
        print(data_hora)


# Implementação do sistema
f1 = Funcionario()
f1.fazer_login()
