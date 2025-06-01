valor1= int(input("O número 1 é:"))
valor2= int(input("O número 2 é:"))
valor3= int(input("O número 3 é:"))
maior= valor1
if valor2 > maior:
    maior = valor2
if valor3 > maior:
    maior = valor3
print("O maior número", maior)