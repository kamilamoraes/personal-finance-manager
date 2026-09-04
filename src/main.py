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
        print("Adicionar receita")

    elif opcao == "2":
        print("Adicionar despesa")

    elif opcao == "3":
        print("Listar transações")

    elif opcao == "4":
        print("Consultar saldo")

    elif opcao == "0":
        print("Encerrando o programa...")

    else:
        print("Opcao inválida.")