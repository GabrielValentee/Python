lista_de_tarefas = []

while True:
    lista = input("Adicione algo na lista de tarefas ou 'sair' para encerrar: ")

    if lista == 'sair':
        break

    lista_de_tarefas.append(lista)
    print(f"O {lista} foi adicionado a lista")

    print("Lista de tarefas final: ")

    for lista in lista_de_tarefas:
            print(".", lista)


