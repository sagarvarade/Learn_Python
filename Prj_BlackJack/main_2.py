import random

suits=["Hearts","Clubs","Spades","Diamonds"]
cards=[]
ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]


for suits in suits:
    for rank in ranks:
       # print([suits,rank])
        cards.append([suits,rank])

def shuffle():
    random.shuffle(cards)

def deal(number):
    cards_deal=[]
    for x in range(number):
        cards_deal.append(cards.pop())
    return cards_deal

shuffle()

cards_deal=deal(5)
card=cards_deal[0]
rank=card[1]


if rank=='A':
    value=11
elif rank=='J' or rank=='Q' or rank=="K":
    value=10
else:
    value=rank

rank_dict={"rank":rank,"value":value}

print(rank,value)
print(rank_dict["rank"],rank_dict["value"])


