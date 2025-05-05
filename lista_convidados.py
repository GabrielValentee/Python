convidados = []

while True:
    nome = input("Digite o nome do convidado ou 'sair' para encerrar: ")

    if nome == 'sair':
        break

    convidados.append(nome)
    print(f"O {nome} foi adicionado a lista")

    if len (convidados) > 5:
        print("Atenção: a lista está ficando grande!")

        print("Lista final de convidados: ")

        for nome in convidados:
            print(".", nome)

print("Total de convidados: 6 ")

