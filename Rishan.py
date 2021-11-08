

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
                HorseID = input("Input horse ID:")
                if 1 <= int(HorseID) <= 256:
                    self.horseID = HorseID
                    print("Id has been set to", self.HorseID)
                    break
                print("Please input valid ID.")
            except ValueError:
                print("Enter an integer")

Horse_Better.SetHorseID()


