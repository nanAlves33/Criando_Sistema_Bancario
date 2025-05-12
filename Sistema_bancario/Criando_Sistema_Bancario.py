"""
Crie um sistema bancario que permita o usuario realizar saque, deposito 
e ver extrato.
Limite de 3 saques diarios e valor de 500€
não ser possivel numeros negativos.
"""


# Variaveis iniciais
saldo = 0
extrato = []
limite_saque = 500
saques_realizados = 0
limite_saques_diarios = 3

def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        extrato.append(f'Depósito: + €{valor:.2f}')
        print(f'✅ Depósito de €{valor:.2f} realizado com sucesso.')
    else:
        print('❌ Valor inválido. O depósito deve ser maior que zero.')

def sacar(valor):
    global saldo, saques_realizados
    if valor <= 0:
        print('❌ Valor inválido. O saque deve ser maior que zero.')
    elif saques_realizados >= limite_saques_diarios:
        print('❌ Limite diário de saques atingido (3 por dia).')
    elif valor > limite_saque:
        print(f'❌ O valor máximo por saque é de €{limite_saque:.2f}.')
    elif valor > saldo:
        print('❌ Saldo insuficiente.')
    else:
        saldo -= valor
        saques_realizados += 1
        extrato.append(f'Saque: -€{valor:.2f}')
        print(f'✅ Saque de €{valor:.2f} realizado com sucesso.')

def ver_extrato():
    print('\n======= EXTRATO =======')
    if not extrato:
        print('Nenhuma movimentação.')
    else:
        for movimento in extrato:
            print(movimento)
    print(f"Saldo atual: €{saldo:.2f}")
    print(f"Saques realizados hoje: {saques_realizados}/3")
    print("=======================\n")

# Menu interativo
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Ver Extrato")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor para depósito: €"))
            depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor para saque: €"))
            sacar(valor)
        elif opcao == "3":
            ver_extrato()
        elif opcao == "4":
            print("✅ Obrigado por usar nosso sistema bancário.")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

# Inicia o programa
menu()
