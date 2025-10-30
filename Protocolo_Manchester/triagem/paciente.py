class Paciente:
    def __init__(self, nome, prioridade, respostas=None):
        self.nome = nome
        self.prioridade = prioridade
        self.respostas = respostas or []

    def __str__(self):
        return f"{self.nome} ({self.prioridade})"
