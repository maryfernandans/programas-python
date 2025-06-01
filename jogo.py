import random

def jogo_adivinhacao():
    print("Bem-vindo ao jogo de Adivinhação!")
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        try:
            palpite = int(input("Digite um número entre 1 e 100: "))
            tentativas += 1
            if palpite < 1 or palpite > 100:
                print("Por favor, digite um número dentro do intervalo.")
                continue
            if palpite == numero_secreto:
                print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
                break
            elif palpite < numero_secreto:
                print("Tente um número maior.")
            else:
                print("Tente um número menor.")
        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    jogo_adivinhacao()