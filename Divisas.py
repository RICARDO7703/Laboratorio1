print("Quetzales", " Q")
print("Dolares", " D")

moneda = input("Seleccione la moneda (Q o D): ")

if moneda == "D":
    n = float(input("Ingrese la cantidad en Q: "))  
    n1 = n / 7.82  
    print(n1 ,"D")

elif moneda == "Q":
    n = float(input("Ingrese la cantidad en D: "))  
    n1 = n * 7.82
    print(n1,"QDD")

else:
    print("Ingrese Q o D")

