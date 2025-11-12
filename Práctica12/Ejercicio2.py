import time

def bomba(tiempo):
    if tiempo == 0:
        print("💥 ¡BOOM! No la detuviste a tiempo.")
        return

    print(f"⏰ La bomba explotará en {tiempo} segundos...")
    accion = input("¿Qué haces? (escribe 'detener' o Enter para esperar): ")

    if accion.lower() == "detener":
        print("🧯 ¡Lograste detener la bomba justo a tiempo!")
        return
    else:
        time.sleep(1)
        bomba(tiempo - 1)  # Llamada recursiva

def jugar_bomba():
    print("=== 💣 JUEGO DE LA BOMBA 💣 ===")
    bomba(5)

jugar_bomba()