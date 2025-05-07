# POO é um paradigma que organiza o código em "objetos", permitindo reutilização e estruturação mais avançada de programas.

# Classes Simples

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}.")

p = Pessoa("Carlos")
p.apresentar()
