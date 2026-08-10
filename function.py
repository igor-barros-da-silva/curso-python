def pedir_valor(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor invalido")

def somar_numeros():
    num1 = pedir_valor("Digite um numero:")
    num2 = pedir_valor("Digite outro numero:")

    soma = num1 + num2
    print(soma)

if __name__ == "__main__":
    somar_numeros()