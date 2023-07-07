menu = """
*******************Banco New*******************
Bem-vindo ao nosso sistema bancário!
Por favor insira as iniciais abaixo para realizar as operações!

[s] Sacar
[d] Depositar
[e] Extrato
[q] Sair

***********************************************
=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("*******************Banco New*******************")
        print("Opção deposito selecionada!")
        deposito = float(input("Informe o valor do deposito: "))
        if deposito >0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito: .2f}\n"
            print("\nAguarde enquanto processamos seu pedido...")
            print(f"\nSeu novo saldo é de R${saldo:.2f}")
            print("Confira o Extrato para mais detalhes!")
            print("Retornando para a tela inicial... Aguarde...")
        else:
           print ("Valor de depósito deve ser positivo!")
        
    




    elif opcao == "s":
        print("*******************Banco New*******************")
        print("Opção de saque selecionada!")
        saque = float (input("Digite a quantidade para sacar:"))

        excedeu_saldo = saque > saldo

        excedeu_limite = saque > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("A operação falhou! Saldo insuficiente")

        elif excedeu_limite:
            print("A operação falhou! Sem limite disponivel")

        elif excedeu_saques:
            print("A operação falhou! Saques insuficiente")

        elif saldo > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque: .2f}\n"
            numero_saques += 1
            print("\nAguarde enquanto processamos seu pedido...")
            print("Saque realizado com sucesso!")
            print(f"\nA sua conta agora possui um novo saldo de R${saldo: .2f}")
            print("Confira o Extrato para mais detalhes!")
            print("Retornando para a tela inicial... Aguarde...")
        
        else:
            print ("A operação falhou! Tente novamente.")





    elif opcao == "e":
        print ("*********EXTRATO**********")
        print ("Não foram realizadas operações!" if not extrato else extrato)
        print (f"Saldo: R$ {saldo: .2f}")
        print("Retornando para a tela inicial... Aguarde...")
        print ("**************************")

    
    
    
    
    
    elif opcao == "q":
        print("*******************Banco New*******************")
        print("Obrigado por usar nossos serviços!")
        print("Volte sempre!")
        print("***********************************************")
        break


        

    else:
        print("Opção inválida. Por favor tente outra opção!.")
