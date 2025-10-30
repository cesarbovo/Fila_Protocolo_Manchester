from utils.menu import exibir_menu, realizar_triagem, ver_fila, atender_paciente

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            realizar_triagem()
        elif opcao == "2":
            ver_fila()
        elif opcao == "3":
            atender_paciente()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()


