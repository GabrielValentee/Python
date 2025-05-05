numeros = []
todos_validos= True

for entrada in range(5):
   entrada = float(input("Insira um número: "))
   numeros.append(entrada)


for numero in numeros:
    if not  [numero > 0 and numero < 100]:
     todos_validos = False
    break


if todos_validos:
    print("Todos os números da lista são positivos e menores que 100.")
else :
    print("Nem todos os números da lista são positivos e menores que 100.")











