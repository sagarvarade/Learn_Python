import random
def getChoices():
    player_choice=input("Enter a choice (rock,paper,scissor) : \n")
    options=["rock","paper","scissor"]
    computer_choice=random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}
    return choices

def check_win(player,computer):
    print(f"You choose {player}, Computer choose {computer}")
    if player==computer:
        return "Its a tie"
    else :
        return "Not matched"

choices=getChoices()
print(choices)

print("Result : ",check_win(choices.get("player"),choices.get("computer")))

food=["pizza","carrots","eggs"]
dinner=random.choice(food)
print(dinner)


# Conditional Statments
a=10
b=20
if a==b and 1==1 or a==10:
    print("a==b")
elif a>b:
    print("a>b")
elif b>a:
    print("b>a")
