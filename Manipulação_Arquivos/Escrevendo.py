# Manipular arquivos permite salvar dados ou ler informações externas, como configurações, relatórios ou registros.

with open("dados.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!\nEste é um arquivo.")
