def lista_de_tarefas():
    tarefas = []

    print("Lista de tarefas")
    print("Digite uma tarefa para adicionar ou digite 'sair' para encerrar.")

    while True:
        tarefa = input("Qual tarefa deseja adicionar? ")

        if tarefa.lower() == 'sair':
            print("Lista final de tarefas:")
            for i, t in enumerate(tarefas, 1):
                print(f"{i}. {t}")
            break
        elif tarefa.strip() == "":
            print("Por favor, digite uma tarefa válida.")
            continue

        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso! Lista atualizada:")
        for i, t in enumerate(tarefas, 1):
            print(f"{i}. {t}")
        print()


lista_de_tarefas()

    
    