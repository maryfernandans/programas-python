# Solicita ao usuário os valores inicial e final em Fahrenheit
valor_inicial = float(input("Digite o valor inicial em Fahrenheit: "))
valor_final = float(input("Digite o valor final em Fahrenheit: "))

# Determina a direção da iteração com base nos valores
if valor_inicial <= valor_final:
    passo = 1  # Incrementa de 1 em 1
    fa_values = range(int(valor_inicial), int(valor_final) + 1)
else:
    passo = -1  # Decrementa de 1 em 1
    fa_values = range(int(valor_inicial), int(valor_final) - 1, passo)

# Imprime o cabeçalho da tabela
print(f"{'Fahrenheit':>12} | {'Celsius':>10}")
print('-' * 25)

# Gera a tabela de conversões
for fa in fa_values:
    celsius = (fa - 32) * 5/9
    print(f"{fa:12.2f} | {celsius:10.2f}")