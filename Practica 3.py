import time

def fifo(procesos):
    print("FIFO\n")
    tiempo_actual = 0
    cola = list(procesos)
    resultado = []
    
    while cola:
        proceso_actual = cola.pop(0)
        tiempo_inicio = max(proceso_actual[1], tiempo_actual)
        tiempo_cpu = proceso_actual[2]
        resultado.append((proceso_actual[0], tiempo_inicio, tiempo_inicio + tiempo_cpu))
        
        proceso_actual = (proceso_actual[0], proceso_actual[1], proceso_actual[2] - tiempo_cpu)
        
        tiempo_actual = tiempo_inicio + tiempo_cpu

        time.sleep(2)
        
        print(f"Proceso: {proceso_actual[0]}, Inicio: {tiempo_inicio}, Finalización: {tiempo_inicio + tiempo_cpu}")

    return resultado


def sjf(procesos):
    print("SJF\n")
    tiempo_total = 0
    tiempo_acumulado = 1

    while procesos:
        # Ordenar los procesos por tiempo de CPU más corto
        procesos.sort(key=lambda x: x[2])

        proceso_actual = procesos.pop(0)
        nombre, tiempo_llegada, tiempo_cpu = proceso_actual
        tiempo_inicio = tiempo_acumulado
        tiempo_ejecucion = tiempo_cpu
        tiempo_acumulado = tiempo_inicio + tiempo_ejecucion
        #print(f"Ejecutando {nombre} durante {tiempo_cpu} unidades de tiempo")

        tiempo_cpu -= tiempo_ejecucion
        #tiempo_total += tiempo_cpu

        # Reducir el tiempo de CPU del proceso actual
        #tiempo_cpu = 0

        # Verificar si hay otros procesos que llegaron durante la ejecución
        procesos = [p for p in procesos if p[2] > tiempo_total]

        if tiempo_cpu > 0:
            procesos.append((nombre, tiempo_llegada, tiempo_cpu))

        time.sleep(2)

        print(f"Proceso: {proceso_actual[0]}, Inicio: {tiempo_inicio}, Finalización: {tiempo_inicio + tiempo_ejecucion}")

def round_robin(procesos, quantum):
    tiempo_actual = 0
    cola = list(procesos)
    resultado = []
    while cola:
        proceso_actual = cola.pop(0)
        tiempo_inicio = max(tiempo_actual, 0 if tiempo_actual == 0 else tiempo_actual)
        tiempo_cpu = min(quantum, proceso_actual[1])

        resultado.append((proceso_actual[0], tiempo_inicio, tiempo_inicio + tiempo_cpu))
        proceso_actual = (proceso_actual[0], proceso_actual[1] - tiempo_cpu)

        tiempo_actual = tiempo_inicio + tiempo_cpu

        #time.sleep(2)

        print(f"Proceso: {proceso_actual[0]}, Inicio: {tiempo_inicio}, Finalización: {tiempo_inicio + tiempo_cpu}")

        if proceso_actual[1] > 0:
            cola.append(proceso_actual)

    return resultado

def cargar_procesos_desde_archivo(nombre_archivo):
    procesos = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            nombre, tiempo_ejecucion, prioridad = linea.strip().split(",")
            procesos.append((nombre, int(tiempo_ejecucion), int(prioridad)))
    # Ordenar procesos por tiempo de llegada de menor a mayor
    procesos = sorted(procesos, key=lambda x: x[1])
    return procesos

def cargar_procesos_desde_archivo2(nombre_archivo):
    procesos = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            nombre, tiempo_ejecucion, prioridad = linea.strip().split(",")
            procesos.append((nombre, int(tiempo_ejecucion), int(prioridad)))
    # Ordenar procesos por tiempo de llegada de menor a mayor
    #procesos = sorted(procesos, key=lambda x: x[1])
    return procesos

if __name__ == "__main__":
    archivo_procesos = "procesos.txt"  # Nombre del archivo de procesos
    quantum = 3
    
    procesos = cargar_procesos_desde_archivo2(archivo_procesos)
    #procesos2 = cargar_procesos_desde_archivo(archivo_procesos)
    #proceso3 = cargar_procesos_desde_archivo(archivo_procesos)
    #resultado2 = sjf(procesos2)
    
    #print("Simulación de Round Robin:")
    #print("Proceso\tInicio\tFinalización")
    
    resultado = round_robin(procesos, quantum)
    #resultado3 = fifo(proceso3)

