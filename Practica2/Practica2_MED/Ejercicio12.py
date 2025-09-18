# Ejercicio 12: Diccionario de estudiante universitario

# Crear diccionario con la información del estudiante
estudiante = {
    "nombre": "Luis",
    "apellido": "Araujo",
    "edad": 20,
    "carrera": "Ingeniería de Software",
    "materias_cursando": ["Programación", "Base de Datos", "Redes"],
    "promedio": 8.5
}

# Agregar 2 materias más a la lista de materias
estudiante["materias_cursando"].append("Ingeniería de Software")
estudiante["materias_cursando"].append("Matemáticas Discretas")

# Modificar el promedio
estudiante["promedio"] = 9.0

# Agregar nueva clave "semestre"
estudiante["semestre"] = 3

# Mostrar la información del estudiante de forma más estética y ordenada
print("=== Información del Estudiante ===")
print(f"Nombre completo: {estudiante['nombre']} {estudiante['apellido']}")
print(f"Edad: {estudiante['edad']} años")
print(f"Carrera: {estudiante['carrera']}")
print(f"Semestre: {estudiante['semestre']}")
print(f"Promedio: {estudiante['promedio']}")
print("Materias cursando:")
for materia in estudiante["materias_cursando"]:
    print(f"  - {materia}")