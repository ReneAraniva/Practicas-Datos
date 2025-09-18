class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0
    def encolar(self, item):
        self.items.append(item)
    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0) if not self.esta_vacia() else None
        
        

cola_red = Cola()
cola_red.encolar("Dispositivo1")
cola_red.encolar("Dispositivo2")
cola_red.encolar("Dispositivo3")
print("Se trasmite:",cola_red.desencolar())
print("Quedan en la cola:",cola_red.items)