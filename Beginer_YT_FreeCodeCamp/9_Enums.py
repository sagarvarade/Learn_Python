from enum import Enum

class State(Enum):
    IN_ACTIVE=0
    ACTIVE=1

print(State.ACTIVE)
print(State(0).value)
print(State(1))
print(State['ACTIVE'].value)
print(list(State))
print(len(State))

age=input("Enter age :")
strAge="Your age is "+age
print(strAge)

