
class Animal:
    def eat(self):
        print("Not Declared")

class Dog(Animal):
    def eat(self):
        print('Eating dog food')

class Cat(Animal):
    def eat(self):
        print('Eating cat food')

animal1=Dog()
animal2=Cat()
animal3=Animal()
animal1.eat()
animal2.eat()
animal3.eat()





