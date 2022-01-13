class Cards():
    def __init__(self, Number, Cards):
        self.__Number = Number
        self.__Cards = Cards 
    def GetNumber(self):
        return self.__Number
    def GetShape(self):
        return self.__Cards
    
OneS = Cards(1,"Square")
TwoS = Cards(1,"Square")
ThreeS = Cards(2,"Circle")

def Compare(Card1, Card2):
    if Card1.GetNumber() == Card2.GetNumber() and Card1.GetShape() == Card2.GetShape():
        print("SNAP")
        return -1
    else:
        if Card1.GetNumber() >= Card2.GetNumber():
            return Card1.GetNumber()
        else:
            return Card2.GetNumber()
        
print(Compare(OneS,ThreeS))
