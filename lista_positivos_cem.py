numeros = ( 15, 80, 55, 20, 95, 30)
todos_validos= True

for numero in numeros:
    if not  [numero > 0 and numero < 100]:
     todos_validos = False
    break


if todos_validos:
    print("Todos os números da lista são positivos e menores que 100.")
else :
    print("Nem todos os números da lista são positivos e menores que 100.")












