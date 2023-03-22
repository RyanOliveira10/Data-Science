from ContaBancaria import ContaPF, ContaPJ

def pessoa_fisica():

    pessoa = ContaPF()

    dados = []

    pessoa.nome = input("Nome : ")
    pessoa.email = input("Email : ")
    pessoa.endereco = input("Endereco : ")
    pessoa.telefone = input("Telefone : ")
    pessoa.numero_conta = input("Numero conta : ")
    pessoa.cpf = input("Cpf: ")

    dados = {'nome': pessoa.nome, 'email' : pessoa.email, 'endereco': pessoa.endereco, 'telefone': pessoa.telefone, 'numero_conta': pessoa.numero_conta, 'cpf': pessoa.cpf}

    for item in dados:
        print(f"\n {item}")

def pessoa_juridica():
    print("pessoa_juridica")

tipo_conta = int(input("1 para pessoa fisica, 2 para pessoa juridica! \n"))
c1 = 'pessoa fisica'
c2 = 'pessao juridica'

if tipo_conta == 1:
    print(f"selecionado : {c1}")
    pessoa_fisica()
else:
    print(f"selecionado : {c2}")
    pessoa_juridica()
