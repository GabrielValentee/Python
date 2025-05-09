class ContaBancaria:
    def __init__(self, numero_conta, saldo_inicial=0):
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado na conta {self.numero_conta}.")
        else:
            print("Valor para depósito inválido.")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado na conta {self.numero_conta}.")
                return True
            else:
                print(f"Erro: Saldo insuficiente na conta {self.numero_conta}.")
                return False
        else:
            print("Valor para saque inválido.")
            return False

    def verificar_saldo(self):
        print(f"Saldo atual da conta {self.numero_conta}: R${self.saldo:.2f}")

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, saldo_inicial=0, limite_cheque_especial=0):

        super().__init__(numero_conta, saldo_inicial)

        self.limite_cheque_especial = limite_cheque_especial
        
        print(f"Conta Corrente {self.numero_conta} criada com limite de cheque especial de R${self.limite_cheque_especial:.2f}.")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo + self.limite_cheque_especial >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado na conta corrente {self.numero_conta}.")
                if self.saldo < 0:
                    print(f"Utilizando cheque especial. Saldo atual: R${self.saldo:.2f}.")
                return True
            else:
                print(f"Erro: Saldo insuficiente (incluindo cheque especial) na conta {self.numero_conta}.")
                return False
        else:
            print("Valor para saque inválido.")
            return False

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_conta, saldo_inicial=0, taxa_juros=0.0):
        super().__init__(numero_conta, saldo_inicial)
        self.taxa_juros = taxa_juros
        print(f"Conta Poupança {self.numero_conta} criada com taxa de juros de {self.taxa_juros * 100:.2f}%.")

    def aplicar_juros(self):
        if self.taxa_juros > 0 and self.saldo > 0:
            juros = self.saldo * self.taxa_juros
            self.saldo += juros
            print(f"Juros de R${juros:.2f} aplicados na conta {self.numero_conta}. Novo saldo: R${self.saldo:.2f}")
        else:
            print(f"Juros não aplicados na conta {self.numero_conta}. Saldo não positivo ou taxa zero.")

conta_corrente = ContaCorrente ("12345-6", 400, 500)

conta_corrente.verificar_saldo()

conta_corrente.depositar(200.0)

conta_corrente.verificar_saldo()

conta_corrente.sacar(500)

conta_corrente.verificar_saldo()

conta_corrente.sacar(800)

conta_corrente.verificar_saldo()

conta_poupanca = ContaPoupanca("78901-2", 500.0, 0.05)

conta_poupanca.verificar_saldo()

conta_poupanca.depositar(300.0)

conta_poupanca.verificar_saldo()

conta_poupanca.sacar(1000.0)

conta_poupanca.sacar(200)