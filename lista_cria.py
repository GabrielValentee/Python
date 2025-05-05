clientes = []

print("=== Cadastro de Clientes do Cinema ===")

while True:
    nome = input("Nome do cliente: ")
    cpf = input("CPF: ")
    temperatura = float(input("Temperatura corporal (°C): "))

    cliente = {
        "nome": nome,
        "cpf": cpf,
        "temperatura": temperatura
    }

    clientes.append(cliente)

    continuar = input("Deseja cadastrar outro cliente? (s/n): ")
    if continuar.lower() != 's':
        break

print("\n=== Clientes Cadastrados ===")
for i, c in enumerate(clientes, 1):
    status = "ALTO RISCO" if c["temperatura"] >= 37.5 else "OK"
    print(f"{i}. {c['nome']} - CPF: {c['cpf']} - Temp: {c['temperatura']}°C ({status})")








    