def calcula_idade(ano_nascimento):
    ano_atual = 2025  # Você pode usar a data atual dinamicamente, se preferir
    idade = ano_atual - ano_nascimento
    return idade

def main():
    ano_nascimento = int(input("Digite o seu ano de nascimento: "))
    idade = calcula_idade(ano_nascimento)
    print(f"Sua idade é: {idade} anos.")

if __name__ == "__main__":
    main()