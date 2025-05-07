try:
    n1 = int(input("Digite o numerador: "))
    n2 = int(input("Digite o denominador: "))
    resultado = n1 / n2
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Erro: divisão por zero!")
