import random
class Crop:
    def __init__(self, growthrate, lightneed, waterneed):
        self._growth = 0
        self._daysgrowing = 0
        self._growthrate = growthrate
        self._lightneed = lightneed
        self._waterneed = waterneed
        self._status = "Seed"
        self._type = "Generic"
    def needs(self):
        print('Light needed: ', self._lightneed)
        print('Water needed: ', self._waterneed)
    def report(self):
        print('---------------------------------')
        print("Status Report.")
        print("Type        : ", self._type)
        print("Status      : ", self._status)
        print("Growth      : ", self._growth)
        print("Days Growing: ",  self._daysgrowing)
        print('---------------------------------')
    def update_status(self):
        if self._growth == 0:
            self._status = "Seed"
        elif self._growth > 0 and self._growth <= 5:
            self._status = "Seedling"
        elif self._growth > 5 and self._growth <= 10:
            self._status = "Young"
        elif self._growth > 10 and self._growth <= 15:
            self._status = "Mature"
        elif self._growth > 15:
            self._status = "Old"
    def grow(self,light,water):
        if light >= self._lightneed and water >= self._waterneed:
            self._growth += self._growthrate
        self._daysgrowing += 1
        self.update_status()
class potato(Crop):
    def __init__(self):
        super().__init__(3,3,3)
        self._type = "Potato"
    def grow(self,light,water):
        if light >= self._lightneed and water >= self._waterneed:
            if self._status == "Seedling" and water> self._waterneed:
                self._growth += self._growthrate * 1.5
            elif self._status == "Young" and water> self._waterneed:
                self._growth += self._growthrate * 1.25
            else:
                self._growth += self._growthrate
        self._daysgrowing += 1
        self.update_status()
class wheat(Crop):
    def __init__(self):
        super().__init__(6,8,7)
        self._type = "Wheat"
    def grow(self,light,water):
        if light >= self._lightneed and water >= self._waterneed:
            if self._status == "Seedling" and water> self._waterneed:
                self._growth += self._growthrate * 2.5
            elif self._status == "Young" and water> self._waterneed:
                self._growth += self._growthrate * 1.8
            else:
                self._growth += self._growthrate
        self._daysgrowing += 1
        self.update_status()
#Crop Display Procedure
def display_menu1():
    print()
    print("Which crop would you like to create?")
    print()
    print("1. Potato")
    print("2. Wheat")
    print()
    print("Select an option from the menu above")
def select_option():
    valid_option = False
    while not valid_option:
        try:
            choice = int(input("Option selected: "))
            if choice in (1,2):
                valid_option = True
            else:
                print("Please enter a valid option.")
        except ValueError:
            print("Please enter a valid option.")
    return choice
def create_crop():
    display_menu1()
    choice = select_option()
    if choice == 1:
        new_crop = potato()
    elif choice == 2:
        new_crop = wheat()
    return new_crop
def main():
    new_crop = create_crop()
    manage_crop(new_crop)
#non - Class Display procedures
def manual_grow(Crop):
    print("Now using manual grow.")
    while True:
        light = int(input("Input a light value from 1-10:"))
        if light < 1 or light >10:
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
main()