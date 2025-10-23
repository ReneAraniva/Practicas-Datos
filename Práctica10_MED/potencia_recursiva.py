# potencia_recursiva.py

def potencia_recursiva(base, exponente):
    """
    Calcula la potencia de un número (base^exponente) de forma recursiva.
    Asume que el exponente es un entero no negativo.
    """
    if exponente == 0:  # Caso base: Cualquier número elevado a 0 es 1
        return 1
    elif exponente < 0:
        # Manejo de exponente negativo (opcional, pero buena práctica)
        return 1 / potencia_recursiva(base, -exponente)
    else:
        # Caso recursivo: base * base^(exponente - 1)
        return base * potencia_recursiva(base, exponente - 1)

# Ejemplo de uso 1: Potencia positiva
base1 = 2
exponente1 = 4
resultado1 = potencia_recursiva(base1, exponente1)
print(f"El resultado de {base1}^{exponente1} es: {resultado1}") # Esperado: 16 (2*2*2*2)

# Ejemplo de uso 2: Potencia cero
base2 = 5
exponente2 = 0
resultado2 = potencia_recursiva(base2, exponente2)
print(f"El resultado de {base2}^{exponente2} es: {resultado2}") # Esperado: 1

# Ejemplo de uso 3: Potencia negativa (ejecuta el elif de manejo)
base3 = 2
exponente3 = -2
resultado3 = potencia_recursiva(base3, exponente3)
print(f"El resultado de {base3}^{exponente3} es: {resultado3}") # Esperado: 0.25 (1/(2^2))