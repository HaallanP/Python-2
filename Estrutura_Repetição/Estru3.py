# Loop infinito com break

# Sai do loop apenas quando o usuário digita 'sair'
while True:
    resposta = input("Digite 'sair' para encerrar: ")
    if resposta.lower() == "sair":
        break
print("Programa encerrado.")
