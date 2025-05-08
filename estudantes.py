estudantes = ["Raimundo", "Abel", "Paulo", "Leonardo"]

print(estudantes)

for nome in estudantes:
    print(f"Os nomes dos estudantes são: {nome}")

print (f"O nome do terceiro estudante é: {estudantes[2]}")

maria = ("Maria", 35, 1.75)
print(maria)


set1 = {"josé", "josé", "Leonardo"}
print(set1)

try:
    numero2 = int(input("Insira um número: "))

    divi = 10 / numero2

    print(divi)

except ValueError:

    print("Dado inválido.Insira um número.")

except ZeroDivisionError:
    print("Opa! Você inseriu 0. Não se pode dividir por 0.")


carro = {
    "cor": "Amarelo",
    "modelo": "camaro",
    "valor": 3.000000,
    "marca": "chevrolet"

}

print(f"{carro['marca']}")