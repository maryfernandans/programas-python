numero1= float(input("O número 1 é:"))
numero2= float(input("O número 2 é:"))
operacao= input("Escolha a operação aritmética: (+, -, *, / )")
if operacao == "+":
     resultado = numero1+ numero2
elif operacao =="-":
   resultado = numero1- numero2
elif operacao == "*":
    resultado = numero1*numero2
elif operacao == "/":
    print("resultado:", resultado)
