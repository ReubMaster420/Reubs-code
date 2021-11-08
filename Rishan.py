

class Horse_Better:
    def __init__(self, InputHorseID):
        self.cash = 0
        self.Horse_level = "N/A"
        self.HorseID = InputHorseID
    def getCash(self):
        return self.cash
    def GetHorseID(self):
        return self.Horse_level
    def GetHorseID(self):
        return self.HorseID

def SetHorseID(self):
    while True:
            try:
                HorseID = str(input("Enter your HorseID:"))
                if int(HorseID) >= 0 and int(HorseID) <= 150:
                    self.HorseID = HorseID
                    print(f"Your new horse id is {self.HorseID}!")
                    break
                print("Must be below/or 456 and above/or 1!")
            except ValueError:
                print('Enter an integer!')

def SetCash(CashInput):
            try:
                if int(CashInput) >= 0 and int(CashInput) <= 150:
                    return True
                return False
            except ValueError:
                print('Enter an integer!')

print(SetCash(0))
#SetHorseID(Horse_Better)



