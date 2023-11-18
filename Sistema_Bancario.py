Menu = """
==============================   MENU  =============================
                        [d] - Depositar
                        [s] - Sacar
                        [e] - Extrato
                        [q] - Sair
====================================================================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(Menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito:"))

        if valor > 0:
            print(f"Deposito realizado com sucesso! R$ {valor:.2f}\n")
            saldo += valor
            extrato += f"Depósito realizado: R$ {valor:.2f}\n"

        else:
            print("operação falhou! O valor informado é inválido.")

    elif opcao == "s":

        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("operação falho! Você não possui saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite")

        elif excedeu_saques:
            print("Operação falhou! Número maximo de saque excedido")

        elif valor > 0:
            print(f"Saque realizado com sucesso! R$ {valor:.2f}\n")
            saldo -= valor
            extrato += f"Saque realizado: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("operação falho! O valor informado é inválido.")

    elif opcao == "e":
        
        print("\n============================== EXTRATO ==============================")
        print("Nao foram realizado movimentações." if not extrato else extrato)
        print (f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================================================")

    elif opcao =="q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")