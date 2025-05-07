class Animal:
    def falar(self):
        print("Som genérico")

class Cachorro(Animal):
    def falar(self):
        print("Au au!")

dog = Cachorro()
dog.falar()
