class Dog:
    # The dogs class
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def __gt__(self,other):
        return True if self.age>other.age else False


rogger=Dog('Roger',8)
syd=Dog('Syd',9)

print(rogger>syd)
print(rogger<syd)

