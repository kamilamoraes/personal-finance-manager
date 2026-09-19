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

def adicionar_transacao(descricao, valor, tipo, data, categoria_id):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("SELECT MAX(id) FROM transacoes")
    ultimo_id = cursor.fetchone()[0]

    novo_id = ultimo_id + 1

    cursor.execute(
        "INSERT INTO transacoes(id, descricao, valor, tipo, data, categoria_id) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        novo_id,
        descricao,
        valor,
        tipo,
        data,
        categoria_id
    )

    conexao.commit()

    cursor.close()
    conexao.close()

def consultar_saldo():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            SUM(CASE WHEN tipo = 'receita' THEN valor ELSE 0 END) -
            SUM(CASE WHEN tipo = 'despesa' THEN valor ELSE 0 END)
        FROM transacoes
    """)

    saldo = cursor.fetchone()[0]

    cursor.close()
    conexao.close()

    return saldo

    
listar_transacoes()

