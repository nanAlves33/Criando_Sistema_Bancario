"""
Crie um sistema bancario que permita o usuario realizar saque, deposito 
e ver extrato.
Limite de 3 saques diarios e valor de 500€
não ser possivel numeros negativos.
"""


# Variaveis iniciais
class Banco:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.limite_saque = 500
        self.saques_realizados = 0
        self.limite_saques_diarios = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +€{valor:.2f}")
            print(f"✅ Depósito de €{valor:.2f} realizado com sucesso.")
        else:
            print("❌ Valor inválido. O depósito deve ser maior que zero.")

    def sacar(self, valor):
        if valor <= 0:
            print("❌ Valor inválido. O saque deve ser maior que zero.")
        elif self.saques_realizados >= self.limite_saques_diarios:
            print("❌ Limite diário de saques atingido (3 por dia).")
        elif valor > self.limite_saque:
            print(f"❌ O valor máximo por saque é de €{self.limite_saque:.2f}.")
        elif valor > self.saldo:
            print("❌ Saldo insuficiente.")
        else:
            self.saldo -= valor
            self.saques_realizados += 1
            self.extrato.append(f"Saque: -€{valor:.2f}")
            print(f"✅ Saque de €{valor:.2f} realizado com sucesso.")

    def ver_extrato(self):
        print("\n======= EXTRATO =======")
        if not self.extrato:
            print("Nenhuma movimentação.")
        else:
            for movimento in self.extrato:
                print(movimento)
        print(f"Saldo atual: €{self.saldo:.2f}")
        print(f"Saques realizados hoje: {self.saques_realizados}/3")
        print("=======================\n")


# Menu interativo com a classe Banco
def menu():
    conta = Banco()

    while True:
        print("\n--- MENU ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Ver Extrato")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor para depósito: €"))
            conta.depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor para saque: €"))
            conta.sacar(valor)
        elif opcao == "3":
            conta.ver_extrato()
        elif opcao == "4":
            print("✅ Obrigado por usar nosso sistema bancário.")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

# Executa o menu
menu()