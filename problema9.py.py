def mom():
    a=str(input("¿Comó se llama la mamá de Goku? "))
    if a == "Gine" or a == "GINE" or a == "gine":
        print("Enhorabuena! La mamá de Goku si se llama",a)
    else:
        print("\n La mamá de Goku no se llama",a,", prueba de nuevo.")
        return mom()

mom()
