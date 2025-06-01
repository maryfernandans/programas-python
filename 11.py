# Cabeçalho da tabela
print(f"{'Fahrenheit':<12} | {'Celsius':<10}")
print('-' * 25)

# Loop de 45 a 80, de 1 em 1
for f in range(45, 81):
    c = 5 * (f - 32) / 9
    print(f"{f:.1f} ºF | {c:.3f} ºC")