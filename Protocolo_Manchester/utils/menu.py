def exibir_menu():
    print("1 - Realizar triagem")
    print("2 - Ver fila de pacientes")
    print("3 - Atender paciente")
    print("4 - Sair")

def realizar_triagem():
    from triagem.arvore import montar_arvore, triagem_arvore
    from triagem.paciente import Paciente
    from triagem.fila import fila_global

    nome = input("Nome do paciente: ")
    arvore = montar_arvore()
    prioridade, respostas = triagem_arvore(arvore)
    paciente = Paciente(nome, prioridade, respostas)
    fila_global.enqueue(paciente)
    print(f"Paciente registrado: {paciente}")

def ver_fila():
    from triagem.fila import fila_global
    if fila_global.tamanho() == 0:
        print("Fila vazia.")
    else:
        print("Fila de pacientes:")
        for p in fila_global.listar_pacientes():
            print(p)

def atender_paciente():
    from triagem.fila import fila_global
    paciente = fila_global.dequeue()
    if paciente:
        print(f"Atendido: {paciente}")
    else:
        print("Fila vazia.")
