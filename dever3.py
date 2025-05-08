# Função que soma três valores
def somar_tres(val1, val2, val3):
    return val1 + val2 + val3


# Função principal
def main():
    # Lendo os três valores inteiros do usuário
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    valor3 = int(input("Digite o terceiro valor: "))

    # Chamando a função de soma
    resultado = somar_tres(valor1, valor2, valor3)

    # Mostrando o resultado
    print("A soma dos três valores é:", resultado)


# Executando a função principal
if __name__ == "__main__":
    main()