def menu():
    menu = """
    ============ Banco New =================
    Bem-vindo ao nosso sistema bancário!
    Por favor insira as iniciais abaixo para realizar as operações!

    [s] Sacar
    [d] Depositar
    [e] Extrato
    [n] Novo usuário
    [nc] Nova conta
    [fc] Filtrar contas
    [q] Sair

    =====================================
    =>"""
    return input((menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato =+ f"Depósito:\tR$ {valor: .2f}\n"
        print("\n Depósito realizado com sucesso!")
    else:
        print("\n A operação falhou! O valor iformardo é inválido.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saque, limite_saques):
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
    return


def extrato():
    print ("*********EXTRATO**********")
    print ("Não foram realizadas operações!" if not extrato else extrato)
    print (f"Saldo: R$ {saldo: .2f}")
    print("Retornando para a tela inicial... Aguarde...")
    print ("**************************")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta cadastrada com sucesso!")
        print("Estamos felizes em ter você conosco!")
        print("Retornando a tela inicial... Aguarde...")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não cadastrado, encerrando cadastro de conta!  ")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []


    while True:
        opcao = menu()
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


        elif opcao =="n":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "fc":
            listar_contas(contas)


        
        
        elif opcao == "q":
            print("*******************Banco New*******************")
            print("Obrigado por usar nossos serviços!")
            print("Volte sempre!")
            print("***********************************************")
            break


            
        else:
            print("Opção inválida. Por favor tente outra opção!.")
main()