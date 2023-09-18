import time

def algoritmo_Prioridades(lista_Procesos):
    print("\nPrioridades\n")
    tiempo_Total = 0

    while lista_Procesos:

        lista_Procesos.sort(key=lambda x: x[2]) #Ordena la lista de menor a mayor usando el atributo de prioridad como la posicion 2

        proceso_Actual = lista_Procesos.pop(0)  #Extrae el primer item de la lista
        nombre, tiempo_Ejecucion, prioridad = proceso_Actual    #Asigna los atributos de cada item en una variable
        tiempo_Inicio = tiempo_Total    #Se asigna el tiempo del proceso a ejecturase y se va actualizando
        tiempo_Ejecucion_Actual = tiempo_Ejecucion  #Se asigna el tiempo del proceso proveniente de la lista
        tiempo_Total = tiempo_Inicio + tiempo_Ejecucion_Actual  #Se suma el tiempo actual y el total para ir actualizando

        tiempo_Ejecucion -= tiempo_Ejecucion_Actual #Se resta el tiempo para actualizar el tiempo de ejecucion del proceso actual

        time.sleep(1)

        print(f"Proceso: {proceso_Actual[0]}, Inicio: {tiempo_Inicio}, Finalización: {tiempo_Inicio + tiempo_Ejecucion_Actual}")

def algoritmo_FIFO(lista_Procesos):
    print("\nFIFO\n")
    tiempo_Actual = 0
    cola = list(lista_Procesos)
    resultado = []
    
    while cola:
        proceso_Actual = cola.pop(0)    #Extrae el primer item de la cola
        tiempo_Inicio = max(tiempo_Actual, 0 if tiempo_Actual == 0 else tiempo_Actual)  #Asigna el tiempo de inicio con la condicional de que si el numero sera 0 si es 0
        tiempo_Ejecucion = proceso_Actual[1]    #Asigna el tiempo de ejecucion del proceso tomandolo como viene en el archivo
        resultado.append((proceso_Actual[0], tiempo_Inicio, tiempo_Inicio + tiempo_Ejecucion))  #Guarda en una lista el proceso con su nombre, tiempo de inicio y su finalizacion
        
        tiempo_Actual = tiempo_Inicio + tiempo_Ejecucion    #Se calcula el tiempo con el cual el proximo proceso comenzara

        time.sleep(1)
        
        print(f"Proceso: {proceso_Actual[0]}, Inicio: {tiempo_Inicio}, Finalización: {tiempo_Inicio + tiempo_Ejecucion}")

    return resultado


def algoritmo_SJF(lista_Procesos):
    print("\nSJF\n")
    tiempo_Total = 0

    while lista_Procesos:
        lista_Procesos.sort(key=lambda x: x[1])
        proceso_Actual = lista_Procesos.pop(0)  #Extrae el primer item de la lista
        nombre, tiempo_Ejecucion, prioridad = proceso_Actual    #Asigna los atributos de cada item en una variable
        tiempo_Inicio = tiempo_Total    #Se asigna el tiempo del proceso a ejecturase y se va actualizando
        tiempo_Ejecucion_Actual = tiempo_Ejecucion  #Se asigna el tiempo del proceso proveniente de la lista
        tiempo_Total = tiempo_Inicio + tiempo_Ejecucion_Actual  #Se suma el tiempo actual y el total para ir actualizando

        tiempo_Ejecucion -= tiempo_Ejecucion_Actual #Se resta el tiempo para actualizar el tiempo de ejecucion del proceso actual

        time.sleep(1)

        print(f"Proceso: {proceso_Actual[0]}, Inicio: {tiempo_Inicio}, Finalización: {tiempo_Inicio + tiempo_Ejecucion_Actual}")

def round_robin(lista_Procesos, quantum):
    print("\nRound Robin\n")
    tiempo_Actual = 0
    cola = list(lista_Procesos)
    resultado = []
    while cola:
        proceso_Actual = cola.pop(0)    #Extrae el primer item de la cola
        tiempo_Inicio = max(tiempo_Actual, 0 if tiempo_Actual == 0 else tiempo_Actual)  #Asigna el tiempo de inicio con la condicional de que si el numero sera 0 si es 0
        tiempo_Ejecucion = min(quantum, proceso_Actual[1])  #Asigna el tiempo de ejecucion, el cual dependiendo su tiempo actual sera menor o igual a 3 por el quantum

        resultado.append((proceso_Actual[0], tiempo_Inicio, tiempo_Inicio + tiempo_Ejecucion)) #Guarda en una lista el proceso con su nombre, tiempo de inicio y su finalizacion
        proceso_Actual = (proceso_Actual[0], proceso_Actual[1] - tiempo_Ejecucion)  #Guarda en una variable todo el proceso despues del resultado anterior para compararlo despues

        tiempo_Actual = tiempo_Inicio + tiempo_Ejecucion    #Se calcula el tiempo con el cual el proximo proceso comenzara

        time.sleep(1)

        print(f"Proceso: {proceso_Actual[0]}, Inicio: {tiempo_Inicio}, Finalización: {tiempo_Inicio + tiempo_Ejecucion}")

        if proceso_Actual[1] > 0:   #Condicional en la que si el tiempo de ejecucion es mayor que 0, el proceso vuelve a la cola
            cola.append(proceso_Actual)

    return resultado

def cargar_Procesos_Desde_Archivo(nombre_archivo):
    procesos = []   #En esta lista se guardan cada uno de los procesos provenientes del archivo
    with open(nombre_archivo, "r") as archivo:  #Esta orden hace que el archivo se abra en modo de lectura
        for linea in archivo:
            nombre, tiempo_Ejecucion, prioridad = linea.strip().split(",")  #Esta instruccion hace que separe por cada "," que encuentre y elimine espacios si es que los tiene
            procesos.append((nombre, int(tiempo_Ejecucion), int(prioridad)))    #Guarda en una variable el proceso listo
    return procesos

archivo_Procesos = "procesos.txt"  #Nombre del archivo de procesos
quantum = 3 #Quantum para el algoritmo RR
    
#Variables para cargar los procesos 
proceso_RR = cargar_Procesos_Desde_Archivo(archivo_Procesos)
proceso_SJF = cargar_Procesos_Desde_Archivo(archivo_Procesos)
proceso_FIFO = cargar_Procesos_Desde_Archivo(archivo_Procesos)
proceso_Prioridades = cargar_Procesos_Desde_Archivo(archivo_Procesos)

#Variables para mostrar los algoritmos
algoritmo_rr = round_robin(proceso_RR, quantum)
algoritmo_sfj = algoritmo_SJF(proceso_SJF)
algoritmo_fifo = algoritmo_FIFO(proceso_FIFO)
algoritmo_prioridades = algoritmo_Prioridades(proceso_Prioridades)
