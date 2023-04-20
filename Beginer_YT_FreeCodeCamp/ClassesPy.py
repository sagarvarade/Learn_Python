
class Animal:
    def walk(self):
        print("Walking")

class Dog(Animal):
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age

    def bark(self):
        print("Woof!",__name__)

roger=Dog("roge",23)
print(type(roger))
print(roger.name," ",roger.age)
roger.bark()
print(roger.bark())
roger.walk()