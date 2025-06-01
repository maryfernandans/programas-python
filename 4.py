# Solicita ao usuário que digite o valor final
valor_final = int(input("Digite o valor final: "))

# Gera a sequência de números naturais até o valor final
sequencia = list(range(1, valor_final + 1))

# Exibe a sequência gerada
print("Sequência gerada:", sequencia)

# Mostra a quantidade de valores na sequência
print("Quantidade de valores na sequência:", len(sequencia))