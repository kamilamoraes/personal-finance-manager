import pyodbc

def conectar_banco():
    conexao = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=PersonalFinanceManager;"
        "Trusted_Connection=yes;"
    )

    return conexao

