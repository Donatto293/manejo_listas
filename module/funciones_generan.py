from random import randint
import os
import module.funcionesConListas as fl

 #funcion que genera una lista de numeros aleatorios hasta que toque 0 y se muestra lo siguiente: la lista, longitud, los numeros pares e impares, la suma de sus valores y el promedio               
def listaHacer():
    os.system("cls")
    #se crea una lista    
    numeros=[]
    #usamos un ciclo while que va a crear la lista de numeros aleatorios
    num2 = 3
    while num2 != 0:
        num2 = randint(0,20)
        #usamos un condicional if para para el ciclo mostrando un mensaje cuando el numero sea 0 y pare el ciclo
        if num2 == 0:
            print("el resultado del numero random es", num2, "\n")
            print(" la lista de numeros es:",numeros,"\n")
            print("la Longitud de la lista es de:", fl.longitudLista(numeros),"\n")   
            fl.impar_ParLista(numeros) 
            print(" ")
            print("la suma de la lista es:", fl.sumarLista(numeros),"\n")  
            print("el promedio de la lista es de:",fl.promediolista(numeros), "\n")
            break
        #en caso de que el numero no sea 0, el numero se agregara a la lista con la funcion append()
        else:
            numeros.append(num2)
    #aqui se imprime los valores llamando a otras funciones
   
    
    
    

         
    
    
            
    
                
                