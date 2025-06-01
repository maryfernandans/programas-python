def mostrar_mensagem_e_numero(mensagem, numero):
    print(f"Mensagem: {mensagem}")
    print(f"Número: {numero}")

def main():
    mensagem = input("Digite a mensagem: ")
    numero = int(input("Digite o número: "))
    mostrar_mensagem_e_numero(mensagem, numero)

if __name__ == "__main__":
    main()