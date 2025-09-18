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
        
cola_hospital = Cola()
cola_hospital.encolar("Paciente1")
cola_hospital.encolar("Paciente2")
cola_hospital.encolar("Paciente3")

print("Atendiendo a:",cola_hospital.desencolar())
print("Quedan en la fila:",cola_hospital.items) 