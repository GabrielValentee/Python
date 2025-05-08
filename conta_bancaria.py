class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0
        print(f"Conta para {self.titular} criada com sucesso!")

    def depositar(self, valor):
        if valor > 0:
                self.saldo += valor
                print(f"Saque de R${valor:2f} realizado. Verifique seu saldo atual: R${self.saldo:2f}")
        else:
                print("Valor de depósito inválido.")
    
    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor de saque inválido.")

    def consultar_saldo(self):
        print(f"Saldo atual de conta de {self.titular}: R${self.saldo:.2f}")

conta_joao = ContaBancaria("João Silva")
conta_joao.depositar(1000)
conta_joao.depositar(500)
conta_joao.consultar_saldo()
