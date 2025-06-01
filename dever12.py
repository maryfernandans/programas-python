def main():
    numeros = []  # Lista para armazenar os números digitados
    while True:
        entrada = input("Digite um número (ou -1 para sair): ")
        try:
            num = int(entrada)
            if num == -1:
                break  # Encerra o loop ao digitar -1
            numeros.append(num)  # Adiciona o número à lista
        except ValueError:
            print("Por favor, digite um número válido.")
    print(f"Quantidade de números digitados: {len(numeros)}")

if __name__ == "__main__":
    main()