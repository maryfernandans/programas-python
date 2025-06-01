# Inicializa o somador
soma = 0

# Loop para percorrer os números múltiplos de 3 até 21
for num in range(3, 22, 3):
    print(num)  # Mostra o número atual
    soma += num  # Soma o número ao somador

# Exibe a soma total
print("A soma dos números múltiplos de 3 até 21 é:", soma)