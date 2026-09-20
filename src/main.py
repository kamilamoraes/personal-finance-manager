from database import listar_transacoes, adicionar_transacao, consultar_saldo

opcao = ""

while opcao != "0":
    print("===== PERSONAL FINANCE MANAGER =====")
    print("1. Adicionar receita")
    print("2. Adicionar despesa")
    print("3. Listar transações")
    print("4. Consultar saldo")
    print("0. Sair")

    opcao = input ("Escolha uma opção:")

    if opcao == "1":
        descricao = input("Descrição da receita: ")
        valor = float(input("Valor da receita: "))
        categoria_id = int(input("ID da categoria: "))
        data = input("Data da receita: ")

       
        adicionar_transacao(
        descricao,
        valor,
        "receita",
        data,
        categoria_id
    )

        print("Receita adicionada:", descricao)
        print("Valor:", valor)
        print("Categoria:", categoria_id)
        print("Data:", data)

    elif opcao == "2":
        descricao = input("Descrição da despesa: ")
        valor = float(input("Valor da despesa: "))
        categoria_id = int(input("ID da categoria: "))
        data = input("Data da despesa: ")

        adicionar_transacao(
            descricao,
            valor,
            "despesa",
            data,
            categoria_id
        )

        print("Despesa adicionada:", descricao)
        print("Valor:", valor)
        print("Categoria:", categoria_id)
        print("Data:", data)

    elif opcao == "3":
        listar_transacoes()

    elif opcao == "4":
        saldo = consultar_saldo()

        print("Saldo:", saldo)

    elif opcao == "0":
        print("Encerrando o programa...")

    else:
        print("Opção inválida.")
        