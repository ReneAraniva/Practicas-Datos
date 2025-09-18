import random

random.seed(42)  # Fijar la semilla para reproducibilidad

clientes = [
    ("Cliente1", random.randint(1, 10)),
    ("Cliente2", random.randint(1, 10)),
    ("Cliente3", random.randint(1, 10)),
    ("Cliente4", random.randint(1, 10)),
    ("Cliente5", random.randint(1, 10))
]

tiempo_acumulado = 0
tiempo_espera = []
tiempo_servicio = []

for nombre, servicio in clientes:
    espera = tiempo_acumulado
    tiempo_espera.append((espera))
    tiempo_servicio.append((servicio))
    print(f"{nombre} - Tiempo de espera: {espera} minutos, Tiempo de servicio: {servicio} minutos")
    
    tiempo_acumulado += servicio
    

promedio_espera = sum(tiempo_espera) / len(clientes)
promedio_servicio = sum(tiempo_servicio) / len(clientes)

print(f"\nTiempo promedio de espera: {promedio_espera:.2f} minutos")
print(f"\nTiempo promedio de servicio: {promedio_servicio:.2f} minutos")