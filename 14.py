soma = 0
for num in range(1, 501):
    if num % 2 != 0 and num % 3 == 0:
        soma += num
print("A soma de todos os números ímpares e múltiplos de três entre 1 e 500 é:", soma)