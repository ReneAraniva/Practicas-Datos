import random

def adivina_numero(secreto, intentos_restantes):
    if intentos_restantes == 0:
        print("❌ Te quedaste sin intentos. El número era:", secreto)
        return

    intento = int(input(f"Adivina el número (te quedan {intentos_restantes} intentos): "))

    if intento == secreto:
        print("🎉 ¡Correcto! Adivinaste el número.")
        return
    elif intento < secreto:
        print("📈 El número secreto es mayor.")
    else:
        print("📉 El número secreto es menor.")

    # Llamada recursiva con un intento menos
    adivina_numero(secreto, intentos_restantes - 1)

def jugar():
    print("=== 🎲 ADIVINA EL NÚMERO 🎲 ===")
    secreto = random.randint(1, 100)
    adivina_numero(secreto, 7)

jugar()