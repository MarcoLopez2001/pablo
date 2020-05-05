def archi():
   
    nom = str(input("\nIngrese el nombre del archivo: "))
    tex = str(input("Ingrese texto a guardar: "))
    file = open(nom,"w")
    file.write(tex)
    file.close()
   
    v = int(input("\nSeleccione 1 para volver a intentar, cualquier otro número para salir: "))
    if v == 1:
        return archi()
    else:
        print("\n\t ¡Gracias!")
        
print("\t\t Explorador de archivos")
archi()
