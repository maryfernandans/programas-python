def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

def main():
    notas = []
    while True:
        entrada = input("Digite a nota do aluno ou -1 para encerrar: ")
        if entrada == "-1":
            break
        try:
            nota = float(entrada)
            notas.append(nota)
        except ValueError:
            print("Por favor, digite um número válido.")
    quantidade_alunos = len(notas)
    media = calcular_media(notas)
    print(f"A média da turma é: {media:.2f}")
    print(f"Quantidade de alunos: {quantidade_alunos}")

if __name__ == "__main__":
    main()