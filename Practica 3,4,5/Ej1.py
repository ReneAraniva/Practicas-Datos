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
        
Cola_estudiantes = Cola()
Cola_estudiantes.encolar("sofia")
Cola_estudiantes.encolar("juan")
Cola_estudiantes.encolar("maria")

print("Entrega primero a:",Cola_estudiantes.desencolar())
print("Queda en la fila:",Cola_estudiantes.items)