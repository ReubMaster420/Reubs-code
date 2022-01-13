class FoodItem():
    def __init__(self, FoodID):
        self.__FoodID = FoodID
        self.__Name = ""
        self.__Calories = 0

    def GetCalories(self):
        return self.__Calories
    def SetCalories(self, Calories):
        if 2000 > Calories > 0:
            self.__Calories = Calories
            return True
        else:
            return False
    
    
