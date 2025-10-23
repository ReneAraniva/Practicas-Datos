# invertir_cadena_recursiva.py

def invertir_cadena(cadena):
    """
    Invierte el orden de una cadena de texto de forma recursiva.
    """
    if len(cadena) <= 1:  # Caso base: Cadena vacía o de un solo carácter
        return cadena
    else:
        # Caso recursivo: Último carácter + invertir el resto de la cadena
        return cadena[-1] + invertir_cadena(cadena[:-1])

# Ejemplo de uso
texto_original = "RECURSIVIDAD"
texto_invertido = invertir_cadena(texto_original)
print(f"Cadena original: {texto_original}")
print(f"Cadena invertida: {texto_invertido}")

# Esperado: DADIVISRUCR