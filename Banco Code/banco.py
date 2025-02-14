from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []

def main() -> None:
    menu()

def menu() -> None:
    
    print("================================")
    print("=====- Bem vindo ao Banco -=====")
    print("================================")

    print("1 - Criar conta")
    print("2 - Efetuar saque")
    print("3 - Efetuar deposito")
    print("4 - Efetuar transferência")
    print("5 - Listar contas")
    print("6 - Sair")

    opcao: int = int(input("Seleciona a opção para prosseguir: "))

    if opcao == 1:
        criar_conta()

    elif opcao == 2:
        efetuar_saque()

    elif opcao == 3:
        efetuar_deposito()

    elif opcao == 4:
        efetuar_transferencia()

    elif opcao == 5:
        listar_contas()
    
    elif opcao == 6:
        print("Volte sempre!!")
        sleep(1)
        exit()
    
    else:
        print("Opção inválida. Tente novamente!")
        print()
        sleep(1)
        menu()
    
    


def criar_conta() -> None:
    
    print("Por favor informe os seguintes dados do cliente")

    nome: str = input("Nome completo: ")
    email: str = input("E-mail: ")
    cpf: str = input("CPF: ")
    data_nascimento: str = input("Data de nascimento: ")

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print("Conta criada com sucesso!")
    print()
    print("Dados da conta:")
    print()
    print(conta)
    sleep(1)
    menu()


def efetuar_saque() -> None:
    
    if len(contas) > 0:
        
        numero_conta: int = int(input("Informe o número da sua conta: "))

        conta: Conta = buscar_conta_por_codigo(numero_conta)

        if conta:

            valor: float = float(input("Informe o valor do saque: "))

            conta.sacar(valor)

        else:
            print(f"A conta {conta} não foi encontrada!")

    else:
        print("Não há contas cadastradas!")
    
    sleep(1)
    menu() 

def efetuar_deposito() -> None:
    
    if len(contas) > 0:
        
        numero_conta: int = int(input("Informe o número da sua conta: "))

        conta: Conta = buscar_conta_por_codigo(numero_conta)

        if conta:

            valor: float = float(input("Informe o valor do deposito: "))

            conta.depositar(valor)

        else:
            print(f"A conta {conta} não foi encontrada!")

    else:
        print("Não há contas cadastradas!")

    sleep(1)
    menu()

def efetuar_transferencia() -> None:
    
    if len(contas) > 0:
        
        numero_conta_origem: int = int(input("Informe o número da sua conta: "))

        conta_origem: Conta = buscar_conta_por_codigo(numero_conta_origem)

        if conta_origem:
            
            numero_conta_destino: int = int(input("Informe o número da conta destino: "))

            conta_destino: Conta = buscar_conta_por_codigo(numero_conta_destino)

            if conta_destino:
                
                valor_transferencia: float = float(input("Informe o valor da transferência: "))

                conta_origem.transferir(conta_destino, valor_transferencia)

            else:
                print(f"A conta destino {conta_destino} não foi encontrada...")

        else:
            print(f"A conta {conta_origem} não foi encontrada!")

    else:
        print("Não há contas cadastradas!")

    sleep(1)
    menu()

def listar_contas() -> None:
    
    if len(contas):
        
        print("=========- Contas -=========")
        print("============================")
        print()

        for conta in contas:
            print(conta)
            sleep(1)

    else:
        print("Não há contas cadastradas!")

    sleep(1)
    menu()

def buscar_conta_por_codigo(numero: int) -> Conta:
    
    conta: Conta = None

    if len(contas) > 0:
        
        for conta in contas:
            if conta.numero_conta == numero:
                conta = conta

    return conta

if __name__ == "__main__":
    main()