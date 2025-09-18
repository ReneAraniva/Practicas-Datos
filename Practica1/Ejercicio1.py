# Definición de variables para aplicar formato de texto en consola (cursiva y reset)
C = "\033[3m"   # Código ANSI para texto en cursiva
R = "\033[0m"   # Código ANSI para resetear el formato

# Impresión de versos con formato en consola
print(f"¨{C}Vivo enamorado de este suelo,{R}")  # Primer verso en cursiva

print(f"¨{C}NO me canso de tu luna y de tu cielo,{R}")  # Segundo verso en cursiva

print(f"¨{C}Porque yo elegí aquí sembrar mis sueños,{R}")  # Tercer verso en cursiva

print(f"¨{C}Porque Dios llenó de magia este pueblo,{R}")  # Cuarto verso en cursiva

print(f"¨{C}Voy desde cipote entre \"la yerba\",{R}")  # Quinto verso en cursiva, incluye comillas escapadas

print(f"¨{C}En mi sangre llevo todos tus paisajes.{R}")  # Sexto verso