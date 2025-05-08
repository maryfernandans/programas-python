def calcular_perimetro(largura, altura):
    """
    Calcula o perímetro de um retângulo.
    Parâmetros:
        largura (float): a largura do retângulo
        altura (float): a altura do retângulo
    Retorna:
        float: o perímetro do retângulo
    """
    return 2 * (largura + altura)

def main():
    print("Cálculo do perímetro de um retângulo")
    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    perimetro = calcular_perimetro(largura, altura)
    print(f"O perímetro do retângulo é: {perimetro}")

if __name__ == "__main__":
    main()