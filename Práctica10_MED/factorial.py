# factorial.py

def factorial(n):
    """
    Calcula el factorial de un número n de forma recursiva.
    n! = n * (n-1)!
    Caso base: 0! = 1 y 1! = 1
    """
    if n == 0 or n == 1:   # Caso base: La condición que detiene la recursión [cite: 7, 20]
        return 1
    else:
        # Caso recursivo: La función se llama a sí misma con un problema más pequeño (n-1) [cite: 8, 23]
        return n * factorial(n - 1)

# Ejemplo de uso
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} ({numero}!) es = {resultado}")