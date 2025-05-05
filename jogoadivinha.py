numero_secreto = 7

print("Que começe os jogos")
print("Tente adivinhar o número que estou pensando de 1 a 10")


palpite = int(input("Fale o seu palpite: "))

if palpite == numero_secreto:
    print("Certa resposta!!!")

elif palpite < numero_secreto:
    print("Tente novamente. O valor está muito abaixo")

else:
    print("Tente novamente. O valor está alto")


