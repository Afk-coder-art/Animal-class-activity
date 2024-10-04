from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("I can walk")

class Snail(Animal):
    def move(self):
        print("I can slither")

dog1 = Dog()
dog1.move()

snake1 = Snail()
snake1.move()