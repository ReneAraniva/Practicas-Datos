# suma_lista_recursiva.py

def suma_recursiva(lista):
    """
    Suma todos los elementos de una lista de números de forma recursiva.
    """
    if not lista:  # Caso base: La lista está vacía
        return 0
    else:
        # Caso recursivo: Primer elemento + suma del resto de la lista (slicing)
        return lista[0] + suma_recursiva(lista[1:])

# Ejemplo de uso
numeros = [2, 4, 6, 8, 10]
resultado = suma_recursiva(numeros)
print(f"La lista a sumar es: {numeros}")
print(f"La suma recursiva de los elementos es: {resultado}")

# Esperado: 2 + 4 + 6 + 8 + 10 = 30