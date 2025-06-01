# Define a função que verifica se o número é positivo, nulo ou negativo
def positivo_nulo_negativo(numero):
    if numero > 0:
        print("Valor Positivo")
    elif numero == 0:
        print("Valor nulo")
    else:
        print("Valor negativo")

# Programa principal
def main():
    # Lê o número do usuário
    num = float(input("Digite um número: "))
    # Chama a função passando o número lido
    positivo_nulo_negativo(num)

# Executa o programa principal
if __name__ == "__main__":
    main()