def valor_absoluto(numero):
    if numero < 0:
        return -numero
    else:
        return numero

# Lê o número digitado pelo usuário
numero_digitado = float(input("Digite um número: "))

# Chama a função passando o número digitado
resultado = valor_absoluto(numero_digitado)

# Exibe o valor absoluto na tela
print("O valor absoluto de", numero_digitado, "é", resultado)