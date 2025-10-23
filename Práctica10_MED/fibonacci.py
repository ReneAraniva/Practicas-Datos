# fibonacci.py

def fibonacci_recursivo(n):
    """
    Calcula el n-ésimo elemento de la serie de Fibonacci de forma recursiva.
    La serie comienza con 0 y 1.
    """
    if n == 0:
        return 0  # Caso base para el primer elemento (índice 0) [cite: 35, 36]
    elif n == 1:
        return 1  # Caso base para el segundo elemento (índice 1) [cite: 37, 38]
    else:
        # Caso recursivo: Suma de los dos elementos anteriores (n-1) + (n-2) [cite: 33, 40]
        # La función se llama recursivamente hasta que n vale 0 o 1 [cite: 44, 45]
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

# Ejemplo de uso
posicion = 7
elemento = fibonacci_recursivo(posicion)
print(f"El elemento en la posición {posicion} de la serie de Fibonacci es: {elemento}") # El elemento 7 es 13 (0, 1, 1, 2, 3, 5, 8, 13, ...) [cite: 46]