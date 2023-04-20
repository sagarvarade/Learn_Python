import random

def get_choices():
    player_choice=input("Enter a choice \n:")
    options=["rock","paper","scissor"]
    computer_choice=random.choices(options)
    choices={"player":player_choice,"computer":computer_choice}
    return choices

# choices=get_choices()
# print(choices)

food=["pizza","carrots","eggs"]
print(random.choice(food))

def check_win(player,computer):
    print(f"you choose {player}, Computer choose {computer}")
    if player==computer:
        return "It's a tie"
    else:
        return "Not matched"


print(check_win(1,1))

a=3
b=3
if a==b:
    print(a," Equals ",b)
elif a!=b:
    print("Not equal")
else:
    print("Not Selected")

age=25
print(f"Sagar is {age} year old.")

dictAry={"player":"rock","computer":"paper"}
dChoice=dictAry["player"]
print("dChoice :",dChoice)
result=check_win(dictAry["player"],dictAry["computer"])
print("Result 2 :",result)
