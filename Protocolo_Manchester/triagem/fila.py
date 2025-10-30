from collections import deque

class Fila:
    def __init__(self):
        self.pacientes = deque()

    def enqueue(self, paciente):
        self.pacientes.append(paciente)
    
    # Novo método para atender paciente segundo prioridade Manchester
    def dequeue(self):
        if not self.pacientes:
            return None
        # Busca paciente de maior prioridade (menor valor)
        paciente = min(self.pacientes, key=lambda p: p.valor_prioridade())
        self.pacientes.remove(paciente)
        return paciente

    def tamanho(self):
        return len(self.pacientes)

    def listar_pacientes(self):
        # Mostra fila ordenada por prioridade para visualização
        return sorted(self.pacientes, key=lambda p: p.valor_prioridade())
    
    def __str__(self):
        return ", ".join(str(p) for p in self.listar_pacientes())

fila_global = Fila()


