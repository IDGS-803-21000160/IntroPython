print("Suma de numeros")

num1=int(input("Ingresa el primer numero"))
num2=int(input("Ingresa el segudo numero"))

if num1 > num2 : 
    print("El {} es mayor que el {}".format(num1,num2))
else:
    print("El {} es mayor que el {}".format(num2,num1))


print("--------------Dame una edad ------------")

edad=int(input("ingresa tu edad"))

if edad>18:
    print("Eres mayor de edad")
elif edad ==18:
    print("Tienes 18")
else:
    print("Eres menor de edad")