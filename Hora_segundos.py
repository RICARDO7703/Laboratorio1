hora = int(input("Ingrese la hora: "))
minutos = int(input("Ingrese los minutos: "))

h = hora * 3600
m= minutos * 60

if hora <=24 and minutos <=60:
    segundos_del_dia = h + m

else:
    print("Intentelo nuevamente")
    
print(f"Han paso {segundos_del_dia} segundos")