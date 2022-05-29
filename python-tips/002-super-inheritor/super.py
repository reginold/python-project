# base super class

class Animal(object):
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hello, I am a {self.name}.")

class Dog(Animal):
    def greet(self):
        super().greet() 
        print('WangWang...')


dog = Dog('dog')
dog.greet()
