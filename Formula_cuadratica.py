import math

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

n = (b**2) - (4*a*c)

x1 = (-b + math.sqrt(n)) / (2*a)
x2 = (-b - math.sqrt(n)) / (2*a)


print(x1)
print(x2)
