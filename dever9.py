# Função para ler os dados de uma pessoa
def ler_pessoa():
    altura = float(input("Digite a altura (em metros): "))
    genero = input("Digite o gênero ('m' para masculino, 'f' para feminino): ").lower()
    return (altura, genero)

# Lista para armazenar os dados do grupo
pessoas = []

# Pergunta ao usuário quantas pessoas há no grupo
n = int(input("Quantas pessoas há no grupo? "))

# Lê os dados de cada pessoa
for _ in range(n):
    pessoa = ler_pessoa()
    pessoas.append(pessoa)

# Extrair as alturas e gêneros usando list comprehensions
alturas = [p[0] for p in pessoas]
generos = [p[1] for p in pessoas]

# Encontrar maior e menor altura usando funções de lista
maior_altura = max(alturas)
menor_altura = min(alturas)

# Contar quantos homens e mulheres usando list comprehensions
quantidade_homens = len([g for g in generos if g == 'm'])
quantidade_mulheres = len([g for g in generos if g == 'f'])

# Exibir os resultados
print(f"\nMaior altura do grupo: {maior_altura} metros")
print(f"Menor altura do grupo: {menor_altura} metros")
print(f"Quantidade de homens: {quantidade_homens}")
print(f"Quantidade de mulheres: {quantidade_mulheres}")