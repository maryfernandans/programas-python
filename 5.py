# Solicita ao usuário que digite o valor inicial
valor_inicial = int(input("Digite o valor inicial: "))

# Gera a sequência de números decrescentes até zero
sequencia = list(range(valor_inicial, -1, -1))

# Exibe a sequência
print("Sequência gerada:", sequencia)

# Exibe a quantidade de valores na sequência
print("Quantidade de valores na sequência:", len(sequencia))