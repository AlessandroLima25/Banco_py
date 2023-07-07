menu = """

[s] Sacar
[d] Depositar
[e] Extrato
[q] Sair

=>"""

saldo = 1500
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
       
       deposito = float(input("Informe o valor do deposito: "))
       
       if deposito >0:
          saldo += deposito
          extrato += f"Depósito: R$ {deposito: .2f}\n"
       else:
           print ("Valor de depósito deve ser positivo!")
        
    elif opcao == "s":
        
        saque = float (input("Digite a quantidade para sacar:"))

        excedeu_saldo = saque > saldo

        excedeu_limite = saque > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Saldo insuficiente")

        elif excedeu_limite:
            print("Sem limite disponivel")

        elif excedeu_saques:
            print("Saques insuficiente")

        elif saldo > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque: .2f}\n"
            numero_saques += 1
            
        else:
            print ("A operação falhou! Tente novamente.")

    elif opcao == "e":

        print(saldo)

    elif opcao == "q":
        break

    else:
        print("Opção inválida. Por favor tente outra opção!.")
