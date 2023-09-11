import time

def round_robin(procesos, quantum):
    tiempo_actual = 0
    cola = list(procesos)
    resultado = []
    
    while cola:
        proceso_actual = cola.pop(0)
        tiempo_inicio = max(proceso_actual[1], tiempo_actual)
        tiempo_ejecucion = min(quantum, proceso_actual[2])
        
        resultado.append((proceso_actual[0], tiempo_inicio, tiempo_inicio + tiempo_ejecucion))
        
        proceso_actual = (proceso_actual[0], proceso_actual[1], proceso_actual[2] - tiempo_ejecucion)
        
        tiempo_actual = tiempo_inicio + tiempo_ejecucion

        time.sleep(2)
        
        print(f"Proceso: {proceso_actual[0]}, Inicio: {tiempo_inicio}, Finalización: {tiempo_inicio + tiempo_ejecucion}")
        
        # Si hay más tiempo en el quantum y tiempo restante en el proceso, el proceso vuelve a entrar
        if proceso_actual[2] > 0:
            cola.append(proceso_actual)
    
    return resultado

def cargar_procesos_desde_archivo(nombre_archivo):
    procesos = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            nombre, tiempo_llegada, tiempo_ejecucion = linea.strip().split(",")
            procesos.append((nombre, int(tiempo_llegada), int(tiempo_ejecucion)))
    # Ordenar procesos por tiempo de llegada de menor a mayor
    procesos = sorted(procesos, key=lambda x: x[1])
    return procesos

if __name__ == "__main__":
    archivo_procesos = "procesos.txt"  # Nombre del archivo de procesos
    quantum = 3
    
    procesos = cargar_procesos_desde_archivo(archivo_procesos)
    
    print("Simulación de Round Robin:")
    print("Proceso\tInicio\tFinalización")
    
    resultado = round_robin(procesos, quantum)

