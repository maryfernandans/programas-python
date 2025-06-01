# Gerar a sequência do dobro dos números naturais até 10
sequencia = [2 * i for i in range(1, 11)]

# Calcular a soma da sequência
soma = sum(sequencia)

# Calcular a média aritmética
media = soma / len(sequencia)

# Exibir os resultados
print("Sequência "
      "do dobro dos números "
      naturais até 10:", sequencia)
print("Soma da sequência:", soma)
print("Média aritmética da sequência:", media)