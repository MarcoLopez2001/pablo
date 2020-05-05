import math
def calculo_media(lista, cantidadN):

    suma=0
    for i in lista:
        suma+=i
    total=suma/cantidadN
    return total

def calculo_moda(lista, cantidadN):
    repeticiones=0
    for i in lista:
        apariciones=lista.count(i)
        if apariciones>repeticiones:
            repeticiones=apariciones
    moda=[]
    for i in lista:
        apariciones=lista.count(i)
        if (apariciones==repeticiones and i not in moda):
            moda.append(i)
    return moda

def calculo_desviacion(lista, cantidadN):
    media=calculo_media(lista, cantidadN)
    lista_sumatoria=[]
    for i in lista:
        distancia=(i-media)**2
        lista_sumatoria.append(distancia)
    sumatoria=sum(lista_sumatoria)
    raiz=sumatoria/cantidadN
    return math.sqrt(raiz)
    
    

cantidadN=int(input("Ingrese el tamaño de la muestra: "))
lista=[]
i=0
while(i<cantidadN):
    numero=int(input("Ingrese numero " + str(i) + ": "))
    lista.append(numero)
    i+=1
print("La media es: " + str("{0:.2f}".format(calculo_media(lista, cantidadN))))
print("La moda es: "+str(calculo_moda(lista, cantidadN)))
print("L desviacion estandar es: " + str("{0:.2f}".format(calculo_desviacion(lista, cantidadN))))
"""con "{0:.2f}".format() limitamos la cantidad de decimales, en este caso solo mostramos dos, si queremos 4 decimales solo modificamos el 2"""
