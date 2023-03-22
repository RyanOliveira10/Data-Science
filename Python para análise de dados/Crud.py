# Para criar uma nova base de dados, é necessário informar o nome. -> concluido
# Para criar uma nova tabela, é necessário informar o nome do banco que receberá a tabela e a DDL de criação. -> parcialmente concluido
# Para excluir uma tabela, é necessário informar o nome do banco e da tabela.

# Para inserir um novo registro em uma tabela, é preciso informar: o nome do banco e da tabela e um dicionário contendo a chave e o valor a ser inserido. Por exemplo, {'nome': 'João', 'idade': 30}.
# Para recuperar, os dados é preciso informar o nome do banco e da tabela.
# Para atualizar um novo registro em uma tabela é preciso informar: o nome do banco e da tabela e dois dicionários, um contendo a chave e o valor a ser atualizado e outro contendo a chave e o valor da condição do registro que será atualizado.
# Para excluir um registro em uma tabela, é preciso informar: o nome do banco e da tabela e um dicionário contendo a chave e o valor da condição para localizar o registro a ser inserido. Por exemplo, {'id_cliente': 10}.

import sqlite3

class Data_Base:
    def __init__(self):
        self.data_base_name = None

    def create_DB(self, data_base_name):
        conn = sqlite3.connect(data_base_name + '.db')
        print(f"Banco de dados {data_base_name} criado com sucesso")
        print(type(conn))

    def create_table(self, data_base_name, name_table):
        
        ddl_create = """
            CREATE TABLE """ + name_table + """ (
                id_fornecedor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                nome_fornecedor TEXT NOT NULL )"""
        
        conn = sqlite3.connect(database=data_base_name + '.db')
        cursor = conn.cursor()
        cursor.execute(ddl_create)

        if cursor == None:
            print("Erro ao criar a tabela")
        else:
            print("Tabela criada com sucesso")

    def delete_table(self):
        return
 

      


# testa a classe Data_base
conexao = Data_Base()
conexao.create_DB('aula')
conexao.create_table('aula', 'fornecedor')
conexao.delete_table('fornecedor')