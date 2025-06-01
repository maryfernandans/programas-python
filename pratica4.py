def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

def main():
    valor = int(input("Digite um número inteiro: "))
    resultado_fatorial = fatorial(valor)
    print(f"O fatorial de {valor} é {resultado_fatorial}")

if __name__ == "__main__":
    main()