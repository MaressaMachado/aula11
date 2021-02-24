#Calculadora que vai receber numero e dizer se é impar ou par
num = int(input("Insira um número: "))
num2 = int(input("Insira um número: "))

def minha_calculadora (calculo):
    if calculo % 2 == 0:
        return ("Par")
    else:
        return ("Impar")
    
print(f"O primeiro número é: {minha_calculadora(num)}"
      f"\nO segundo número é: {minha_calculadora(num2)}")


