import random
class Character:
    def __init__(self):
        self.name = ""
        self.attack = 0
        self.defence = 0
        self.__health = 0 #Demo private attribute
        self.experience = 0
        self.racistlvl = 0
    def print_basics(self):
        print("\nName:       ",self.name)
        print("attack:     ",self.attack)
        print("defence     ",self.defence)
        print("health:     ",self.__health)
        print("experience: ",self.experience)
        print("racistlvl:  ",self.racistlvl)
    def setter(self,name):
        self.name = name
        self.attack = random.randint(10,20)
        self.defence = random.randint(10,20)
        self.__health = random.randint(10,20)
    def health_getter(self):
        return self.__health
    def print_me(self):
        self.print_basics()
    def print_intro(self):
        print('This is an exciting story')

class wizard(Character):
    def __init__(self):
        Character.__init__(self) #need to add in parent classes
        self.magic = 0
    def setter(self,name):
        self.name = name
        self.attack = random.randint(20,30)
        self.defence = random.randint(20,30)
        self.__health = random.randint(20,30)
        self.magic = 30
    def health_getter(self):
        return self.__health
    def print_me(self):
        self.print_basics()
        print("magic:      ",self.magic)

class knight(Character):
    def __init__(self):
        Character.__init__(self) #need to add in parent classes
        self.armour = 0

    def setter(self,name):
        self.name = name
        self.attack = random.randint(20,30)
        self.defence = random.randint(20,30)
        self.__health = random.randint(20,30)
        self.armour = 30

    def health_getter(self):
        return self.__health

    def print_me(self):
        self.print_basics()
        print("armour:      ",self.armour)

caste = input("Are you a Knight('K') or a Wizard('W')")
char_name = input("What do you go by?")

if caste.upper() == 'K':
    print("Oh wow a Knight")
    you = knight()
elif caste.upper() == "W":
    print("Nice hat dude")
    you = wizard()
else:
    print("Oh you stutter too much peasant")
    you = Character()

you.setter(char_name)
you.print_me()
print(you.health_getter())