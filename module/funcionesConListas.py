"""
SENA centro de biotecnologia agropecuaria
Ficha:2877795
Aprendiz: Kevin Donato Jimenez Rocha
version: 1.0
fecha: 25/04/2024
"""

#funcion Recorre una lista y la imprime a pantalla
def recorrerLista(lista):
    for i in lista:
        print(i)


#funcion que sirve en una lista numerica ya que imprimira que numero es par y cual impar en pantalla        
def impar_ParLista(lista):
    #con un ciclo for que recorre la lista realizara con cada valor una operacion que servira para saber si es par o impar con una condicion if
    for i in lista:
        n = (i // 2)*2
        if n == i:
            print(i, "es par")
        else:
            print(i, "es impar")
 
#funcion que suma los valores de una lista con un ciclo for            
def sumarLista(lista):
    resultado= 0
    for i in lista:
        
        resultado = resultado + i
    #retornamos el resultado de la suma    
    return resultado    
    
# funcion que saca el promedio de una lista numerica    
def promediolista(lista):
    #encerramos en variables los valores de las funciones para la longitud y suma de una lista
    cantidadValores = longitudLista(lista)
    sumaValores = sumarLista(lista)
    #realizamos la operacion para sacar el promedio con las variables antes nombradas
    if cantidadValores == 0:
        print ("el promedio es 0")
        promedio= 0
    else:
        promedio= sumaValores/cantidadValores
    #retornamos el promedio
    return promedio
    
    
#funcion que cuenta la cantidad de valores de la lista    
def longitudLista(lista):
    longitud= 0
    for element in lista:
        longitud +=1
    #retornamos la longitud    
    return longitud