fila_de_atendimento = []

print("Chegada de Clientes")
while True:
    chegada = input("Digite 'sim' para um novo cliente ou 'fim' para encerrar: ")
    if chegada == 'sim':
        nome_cliente = input("Digite o nome do cliente: ")
        fila_de_atendimento.append(nome_cliente)
        print("Fila atual:", fila_de_atendimento)
    elif chegada == 'fim':
        break
    else:
        print("Entrada inválida.")

        print("Atendimento de Clientes")
while fila_de_atendimento:
    atendimento = input("Digite 'atender' para chamar o próximo cliente ou 'fim' para encerrar o atendimento: ")
    if atendimento == 'atender':
        cliente_atendido = fila_de_atendimento.pop(0)
        print(f"Atendendo o cliente: {cliente_atendido}")
        print("Fila restante:", fila_de_atendimento)
    elif atendimento == 'fim':
        break
    else:
        print("Entrada inválida.")

print("Sistema de Atendimento Encerrado")
    

    
 



