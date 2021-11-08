

class Horse_Better:
    def __init__(self, InputHorseID):
        self.cash = 0
        self.Horse_level = "N/A"
        self.HorseID = InputHorseID
    def getCash(self):
        return self.cash
    def GetHorseLevel(self):
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
    def SetCash(self, CashInput):
            try:
                if int(CashInput) >= 0 and int(CashInput) <= 150:
                    self.cash = CashInput
                    return True
                return False
            except ValueError:
                print('Enter an integer!')
    def SetHorse_Level(self):
        if 1<= self.cash <= 45:
            self.Horse_level = "Pathetic"
        if 46<= self.cash <= 90:
            self.Horse_level = "Mid"
        if 91<= self.cash <= 130:
            self.Horse_level = "Good"
        if 131<= self.cash <= 150:
            self.Horse_level = "Insane"
        

def Timothee_Chalamet():
    Chalamet = Horse_Better(1)
    Chalamet.SetCash(150)
    Chalamet.SetHorse_Level()
    Chalamet.SetHorseID()

def Fibonacci(n): #Takes a parameter n as the nth term of the fibonacci sequence
	if n==0: 
		return(0) #0 is the first term
	elif n==1: 
		return(1)	##base cases #1 is the second term
	else: 
		return Fibonacci(n-1) + Fibonacci(n-2) #This is the recursive part where the 2nd term is (0th)=0 + (1st)=1 and hence 3rdh term is 1st(1) + 2nd(1)

def CreateHorse():
    Nicq = Horse_Better(20)
    Nicq.SetCash(20)
    Nicq.SetHorse_Level()
    print(Nicq.GetHorseLevel())

CreateHorse()
