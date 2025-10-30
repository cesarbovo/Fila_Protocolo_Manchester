class NodoArvore:
    def __init__(self, pergunta=None, cor=None):
        self.pergunta = pergunta
        self.cor = cor
        self.sim = None
        self.nao = None

def montar_arvore():
    # Manchester priorizando emergência
    raiz = NodoArvore("O paciente está respirando?")
    nodo_vermelho = NodoArvore(cor="Vermelho")
    nodo_consciente = NodoArvore("O paciente está consciente?")
    nodo_dor = NodoArvore("O paciente está com dor intensa (8-10)?")
    nodo_laranja = NodoArvore(cor="Laranja")
    nodo_amarelo = NodoArvore(cor="Amarelo")
    nodo_verde = NodoArvore("Caso de rotina ou problema simples?")
    nodo_azul = NodoArvore(cor="Azul")
    nodo_verde_final = NodoArvore(cor="Verde")

    # Ligação da árvore
    raiz.sim = nodo_consciente       # Se respirando → pergunta consciência
    raiz.nao = nodo_vermelho         # Se NÃO respirando → vermelho

    nodo_consciente.sim = nodo_dor      # Se consciente → pergunta dor intensa
    nodo_consciente.nao = nodo_laranja  # Se NÃO consciente → laranja

    nodo_dor.sim = nodo_amarelo         # dor intensa → amarelo
    nodo_dor.nao = nodo_verde           # se não → pode ser verde ou azul

    nodo_verde.sim = nodo_azul         # Se rotina/problema simples → azul
    nodo_verde.nao = nodo_verde_final  # Se não → verde

    return raiz

def triagem_arvore(raiz):
    nodo = raiz
    respostas = []
    while nodo.cor is None:
        resposta = input(f"{nodo.pergunta} (s/n): ").strip().lower()
        respostas.append(resposta)
        if resposta == 's':
            nodo = nodo.sim
        else:
            nodo = nodo.nao
    return nodo.cor, respostas
