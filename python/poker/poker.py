#Straight Flush
#Four of a Kind
#Full House
#Flush
#Straight
#Three of a Kind
#Two Pair
#1 Pair
#High Card
#["4S 5S 7H 8D JC"]
#suits=S, S, H, D, C
def isFlush(suits):
    for card in suits:
        if card != suits[0]:
            return False
    return 

def handType(hand):
    suits=[]
    values=[]
    hand=hand.split()
    
    for card in hand:
        values.append(card[0])
        suits.append(card[1])

def best_hands(hands):
    pass

