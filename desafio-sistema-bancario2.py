
def menu():
    menu = """
    === Seja Bem Vindo! Estou aqui para te ajudar ===
    
    Por favor, me diga o número da opção desejada!

[1] Depositar
[2] Sacar
[3] Extrato

=== Opções Para Funcionários ===

[4] Novo usuário
[5] Nova conta
[9] Sair
=> """
    return input(menu)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:R$ {valor:.2f}\n"
        print("""
              === Depósito realizado com sucesso! ===
              
              """)
    else:
        print("""
              ====== Operação falhou! ======1
              O valor informado é inválido!
              Por favor reinicie a operação! """)
        
    return saldo, extrato

        
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("""
                ====== Operação falhou! ======
                  
                Você não tem saldo suficiente.""")

    elif excedeu_limite:
        print("""
                ====== Operação falhou! ======
                  
            O Valor Máximo por saque é R$ 500.
                  
             Por favor reinicie a operação!""")

    elif excedeu_saques:
         print("""
                     ====== Operação falhou! ======
                  
                Você excedeu o limite de saques diário.""")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("""
                ====== Operação falhou! ======
                  
                  Informe um valor válido.""")

    return saldo, extrato  

def exibir_extrato(saldo, /, *, extrato):
   print("\n================ EXTRATO ================")
   print("Não foram realizadas movimentações." if not extrato else extrato)
   print(f"\nSaldo: R$ {saldo:.2f}")
   print("\nObrigado por ultilizar nossos terminais de auto-atendimento! ")
   print("\n==========================================")

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
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

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

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
               saldo += valor
               extrato += f"Depósito: R$ {valor:.2f}\n"

            else:
              print("Operação falhou! O valor informado é inválido.")


            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
               contas.append(conta)

        
        elif opcao == "9":
            break

        else:
            print("Opção inválida, por favor selecione novamente a opção desejada.")


main()