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
        
        print("Receita adicionada:", descricao)
        print("Valor:", valor)
        print("Categoria:", categoria)
        print("Data:", data)

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