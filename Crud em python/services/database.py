import pyodbc

server = 'tcp:myserver.database.windows.net'
database = ''
username = ''
password = ''
conexao = pyodbc.connect('DRIVER={OBDC Driver 19 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = conexao.cursor()