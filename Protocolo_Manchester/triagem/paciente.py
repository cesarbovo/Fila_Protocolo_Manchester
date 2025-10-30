class Paciente:
    PRIORIDADE_MANCHESTER = {
        "vermelho": 1,
        "laranja": 2,
        "amarelo": 3,
        "verde": 4,
        "azul": 5
    }
    
    def __init__(self, nome, prioridade, respostas=None):
        self.nome = nome
        self.prioridade = prioridade.lower()  # garante minúsculas
        self.respostas = respostas or []
    
    def valor_prioridade(self):
        return Paciente.PRIORIDADE_MANCHESTER.get(self.prioridade, 100)
    
    def __str__(self):
        return f"{self.nome} ({self.prioridade})"


