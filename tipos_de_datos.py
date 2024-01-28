print("""Ingrese datos en el siguiente orden
      Int
      Float
      String""")


try:
    dato = int(input("Ingrese un dato entero: "))
    dato2 = float(input("Ingrese un dato decimal: "))
    dato3 = input("Ingrese un string: ")

    if type(dato) == int:
        if type(dato2) == float:
            if type(dato3) == str:
                print("Ingreso los datos correctamente")
            else:
                print("Ingreso otro tipo de dato")
        else:  
            print("Ingreso otro tipo de dato")
    
    else:
        print("Ingreso otro tipo de dato")

except ValueError:
    print("Ingreso otro tipo de dato")
