print("Celsius", " C")
print("Fahrenheit", " F")

temperatura = input("Seleccione la temperatura (C o F): ")
n = float(input("Ingrese la temperatura: "))  

if temperatura == "C":
    n1 = (n * 1.8) + 32

elif temperatura == "F":
    n1 = (n - 32) / 1.8  

else:
    print("Ingrese C o F")

print(n1, temperatura)
