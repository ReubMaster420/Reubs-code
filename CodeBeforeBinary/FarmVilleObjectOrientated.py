import random
class Crop:
    def __init__(self, growthrate, lightneed, waterneed):
        self.__growth = 0
        self.__daysgrowing = 0
        self.__growthrate = growthrate
        self.__lightneed = lightneed
        self.__waterneed = waterneed
        self.__status = "Seed"
        self.__type = "Generic"
    def needs(self):
        print('Light needed: ', self.__lightneed)
        print('Water needed: ', self.__waterneed)
    def report(self):
        print('---------------------------------')
        print("Status Report.")
        print("Type        : ", self.__type)
        print("Status      : ", self.__status)
        print("Growth      : ", self.__growth)
        print("Days Growing: ",  self.__daysgrowing)
        print('---------------------------------')
    def update_status(self):
        if self.__growth == 0:
            self.__status = "Seed"
        elif self.__growth > 0 and self.__growth <= 5:
            self.__status = "Seedling"
        elif self.__growth > 5 and self.__growth <= 10:
            self.__status = "Young"
        elif self.__growth > 10 and self.__growth <= 15:
            self.__status = "Mature"
        elif self.__growth > 15:
            self.__status = "Old"
    def grow(self,light,water):
        if light >= self.__lightneed and water >= self.__waterneed:
            self.__growth += self.__growthrate
        self.__daysgrowing = self.__daysgrowing + 1
        self.update_status()

class potato(Crop):
    def __init__(self):
        super().__init__(1,3,6)
        self._type = "1"

#non Class procedures


def manual_grow(Crop):
    print("Now using manual grow.")
    while True:
        light = int(input("Input a light value from 1-10:"))
        if 1 > light > 10:
            print("Light value not within set parameters!")
        else:
            break
    while True:
        water = int(input("Input a water value from 1-10:"))
        if 1 > water > 10:
            print("water value not within set parameters!")
        else:
            break
    print("Light value recognised as", light)
    print("Water value recognised as", water)
    Crop.grow(light,water)
        

def auto_grow(Crop, days):
    print("Now using autogrow.")
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        Crop.grow(light,water)
    print("Auto grow has been used for", days,"days.")
    
def display_menu():
    print("1. Grow manually over 1 day.")
    print("2. Autogrow over 30 days.")
    print("3. Report status.")
    print("0. Exit test program.")
    print()
    print("Select an option from the menu above")

def get_menu_choice():
    while True:
        choice = int(input("Input a number from the list(0-3)."))
        if 0 <= choice <= 3:
            return choice
            break
        else:
            print("Input a valid option.")

def manage_crop(Crop):
    print("This is the crop management program.")
    print()
    while True:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(Crop)
            print()
        elif option == 2:
            auto_grow(Crop, 30)
            print()
        elif option == 3:
            Crop.report()
            print()
        elif option == 0:
            break
    print()
    print("Thanks for using the crop management program.")
    


def mainCrop():
    #new_crop = Crop(5,4,3)
    #manage_crop(new_crop)
    potato_crop = potato()
    print(potato_crop.report())
    manual_grow(potato_crop)
    print(potato_crop.report())




mainCrop()