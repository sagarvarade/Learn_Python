def getChoices():
    player_choice="rock"
    computer_choice="paper"
    print("Function called",player_choice," ",computer_choice)

def returnPlayer():
    code="Test Player"
    return code

getChoices() # Calling function
getPlayer=returnPlayer() # Get player is called and value assign to variable
print("The player is :",getPlayer)

def greeting():
    return "Hi You are greet here !"

resp=greeting()
print(resp)

# Dictionary example
dict={"name":"beau","color":"blue"}
def returnFromDict(key):
    return dict.get(key)


print("Dict",dict)
print("dictionary Get : ",dict.get("name"))
print("Dict",returnFromDict("color"))


