try:
    numero = int(input("Digite um número inteiro: "))
    print("Você digitou:", numero)
except ValueError:
    print("Valor inválido.")
