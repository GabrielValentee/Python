cpf1= "702.698.651-01"
print("Seja bem vindo a nosa empressa: ")

name= input("Qual é o seu nome? ")
print(f"Seja bem vindo, {name}")

cpf= input("digita o seu CPF: ")

print(f"seu cpf é {cpf}.")

mum = int(input("digite seu numero: "))

print(f"Seu nuúmero de telefone é {mum}")

email= input("Informe seu email: ")

id = input("qual é a sua idade?")

id = int(id)


if cpf == cpf1 :
    print("clinte ja existe com esse cpf")

else :
    print("cpf valido")

if id <= 18 :
    print("Voce é menor de idade: ") 

else:
    print("pode continuar")

get_opcao = input(" tecle 1 - Quero uma vaga de emprego , tecle 2 - Quero fazer uma compra ")
opcao=int(get_opcao)



if opcao == 1:
    print("okay, iremos verificar")
elif opcao == 2:
    print("okay, so um instante")
