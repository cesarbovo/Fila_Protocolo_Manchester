from collections import deque

class Fila:
    def __init__(self):
        self.pacientes = deque()

    def enqueue(self, paciente):
        self.pacientes.append(paciente)

    def dequeue(self):
        return self.pacientes.popleft() if self.pacientes else None

    def tamanho(self):
        return len(self.pacientes)

    def listar_pacientes(self):
        return list(self.pacientes)

    def __str__(self):
        return ", ".join(str(p) for p in self.pacientes)

fila_global= Fila()
