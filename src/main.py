transacoes = []

opcao = ""

while opcao != "0":
    print("===== PERSONAL FINANCE MANAGER =====")
    print("1. Adicionar receita")
    print("2. Adicionar despesa")
    print("3. Listar transações")
    print("4. Consultar saldo")
    print("0. Sair")

    opcao = input ("Escolha uma opção: ")

    if opcao == "1":
        descricao = input("Descrição da receita: ")
        valor = float(input("Valor da receita: "))
        categoria = input("Categoria da receita: ")
        data = input("Data da receita: ")

        receita = {
            "descricao": descricao,
            "valor": valor,
            "categoria": categoria,
            "data": data,
            "tipo": "receita"
        }

        transacoes.append(receita)

        print("Receita adicionada:", descricao)
        print("Valor:", valor)
        print("Categoria:", categoria)
        print("Data:", data)

    elif opcao == "2":
        descricao = input("Descrição da despesa: ")
        valor = float(input("Valor da despesa: "))
        categoria = input("Categoria da despesa: ")
        data = input("Data da despesa: ")

        despesa = {
            "descricao": descricao,
            "valor": valor,
            "categoria": categoria,
            "data": data,
            "tipo": "despesa"
        }

        transacoes.append(despesa)

        print("Despesa adicionada:", descricao)
        print("Valor:", valor)
        print("Categoria:", categoria)
        print("Data:", data)

    elif opcao == "3":
        for transacao in transacoes:
            print("Descrição:", transacao["descricao"])
            print("Valor:", transacao["valor"])
            print("Categoria:", transacao["categoria"])
            print("Data:", transacao["data"])
            print("Tipo:", transacao["tipo"])
            print("-------------------------")

    elif opcao == "4":
        saldo = 0

        for transacao in transacoes:
            if transacao["tipo"] == "receita":
                saldo += transacao["valor"]

            elif transacao["tipo"] == "despesa":
                saldo -= transacao["valor"]

        print("Saldo:", saldo)

    elif opcao == "0":
        print("Encerrando o programa...")

    else:
         print("Opção inválida.")
        