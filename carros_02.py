def lista_de_carros():
    carros = []

    print("Cadastro de carros")
    print("Digite os dados do carro ou 'sair' no modelo para encerrar.\n")

    while True:
        modelo = input("Modelo: ")
        if modelo.lower() == 'sair':
            break

        marca = input("Marca: ")
        ano = input("Ano: ")
        cor = input("Cor: ")

        carro = {
            "modelo": modelo,
            "marca": marca,
            "ano": ano,
            "cor": cor
        }

        carros.append(carro)
        print("\nCarro adicionado com sucesso! Lista atualizada:\n")

        for i, c in enumerate(carros, 1):
            print(f"{i}. Modelo: {c['modelo']}, Marca: {c['marca']}, Ano: {c['ano']}, Cor: {c['cor']}")
        print()

lista_de_carros()

