# Solicita ao usuário que informe um número inteiro
numero = int(input("Digite um número inteiro: "))

print(f"Tabuada de {numero}:")

# Gera a tabuada de 1 a 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")