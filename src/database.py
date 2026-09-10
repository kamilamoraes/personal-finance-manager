import pyodbc

def conectar_banco():
    conexao = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=PersonalFinanceManager;"
        "Trusted_Connection=yes;"
    )

    return conexao

def listar_transacoes():
    conexao = conectar_banco()

    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM transacoes")

    transacoes = cursor.fetchall()

    for transacao in transacoes:
        print(transacao)

    cursor.close()
    conexao.close()

