def soma(a, b):
    resultado = a + b
    print(f"O resultado de {a} + {b} é {resultado}")

def subtracao(a, b):
    resultado = a - b
    print(f"O resultado de {a} - {b} é {resultado}")

def multiplicacao(a, b):
    resultado = a * b
    print(f"O resultado de {a} x {b} é {resultado}")

def divisao(a, b):
    if b != 0:
        resultado = a / b
        print(f"O resultado de {a} / {b} é {resultado}")
    else:
        print("Erro: divisão por zero não é permitida.")

def main():
    operacao = input("Digite a operação desejada (+, -, x, /): ")
    a = float(input("Digite o primeiro valor: "))
    b = float(input("Digite o segundo valor: "))

    if operacao == '+':
        soma(adef soma(a, b):
    resultado = a + b
    print(f"O resultado de {a} + {b} é {resultado}")

def subtracao(a, b):
    resultado = a - b
    print(f"O resultado de {a} - {b} é {resultado}")

def multiplicacao(a, b):
    resultado = a * b
    print(f"O resultado de {a} x {b} é {resultado}")

def divisao(a, b):
    if b != 0:
        resultado = a / b
        print(f"O resultado de {a} / {b} é {resultado}")
    else:
        print("Erro: divisão por zero não é permitida.")

def main():
    operacao = input("Digite a operação desejada (+, -, x, /): ")
    a = float(input("Digite o primeiro valor: "))
    b = float(input("Digite o segundo valor: "))

    if operacao == '+':
        soma(a, b)
    elif operacao == '-':
        subtracao(a, b)
    elif operacao == 'x':
        multiplicacao(a, b)
    elif operacao == '/':
        divisao(a, b)
    else:
        print("Operação inválida. Por favor, escolha entre +, -, x ou /.")

if __name__ == "__main__":
    main(), b)
    elif operacao == '-':
        subtracao(a, b)
    elif operacao == 'x':
        multiplicacao(a, b)
    elif operacao == '/':
        divisao(a, b)
    else:
        print("Operação inválida. Por favor, escolha entre +, -, x ou /.")

if __name__ == "__main__":
    main()