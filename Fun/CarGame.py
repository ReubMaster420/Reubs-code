import random
from re import L
class team:
    def __init__(self,name, money, sponsors, experience, points):
        self.__name = name
        self.__money = money
        self.__sponsors = sponsors
        self.__experience = experience
        self.__points = points    
    def __repr__(self):
        return self.__name 
    def stats(self):
        print("Team Name:", self.__name)
        print("Points:",self.__points)
        print("Money:",self.__money)
        print("Sponsors:",self.__sponsors)
        print("Experience:",self.__experience)
    def gname(self):
        return self.__name 
    def gmoney(self):
        return self.__money
    def gsponsors(self):
        return self.__sponsors
    def gexperience(self):
        return self.__experience
    def gpoints(self):
        return self.__points

class track():
    def __init__(self, trackname):
        self.__trackname = trackname
        self.__laps = random.randint(50,80)
        self.__laptimeavg = random.randint(60,90)
        self.__corners = random.randint(12,20)
    def __repr__(self):
        return self.__trackname
    def stats(self):
        print("Track name:", self.__trackname)
        print("Laps:",int(self.__laps))
        print("Reference lap time:",self.__laptimeavg)
        print("Number of corners:",self.__corners)
    def laps(self):
        return self.__laps
    def laptime(self):
        return self.__laptimeavg
    def corners(self):
        return self.__corners


class car(team):
    def __init__(self, owner):
        self.__owner = owner + " 001"
        self.__drag = 1.1
        self.__horsepower = 1000
        self.__grip = 5
        self.__handling = 5
        self.__rating = 0
    def carset(self, experience, money, sponsors):
        self.__drag = self.__drag*(100/experience)
        self.__horsepower = self.__horsepower + money 
        self.__grip = self.__grip + sponsors
        self.__handling = self.__grip*experience
        self.__rating = self.__horsepower + self.__grip*100 +self.__handling*50 - self.__drag*100
    def __repr__(self):
        return self.__owner    
    def stats(self):
        print("Car name:", self.__owner)
        print("Car Rating",int(self.__rating))
        print("Horsepower:",self.__horsepower)
        print("Grip:",self.__grip)
        print("Handling:",self.__handling)
        print("Drag:",self.__drag)
    def gowner(self):
        return self.__owner
    def gdrag(self):
        return self.__drag
    def ghorse(self):
        return self.__horsepower
    def ggrip(self):
        return self.__grip
    def ghandling(self):
        return self.__handling
    def grating(self):
        return self.__rating

Teams = ["Ferarri","Mercedes","Mclaren","Aston Martin","Renault","Haas","Williams","Alpha Tauri"]
cars = []
cars2 = []
Tracks = ["Austia", "Silverstone","Canada","Australia","Mexico","USA","Italy","Turkey","Japan","Malaysia"]
for i in range(len(Teams)):
    Teams[i] = team(Teams[i],random.randint(50,130),random.randint(4,20),random.randint(30,100),0)
for i in range(len(Tracks)):
    Tracks[i] = track(Tracks[i])


def insertion():
    for i in range(len(Teams)):
        currentmoney = Teams[i].gmoney()
        currentteam = Teams[i]
        j = i - 1
        while j >= 0 and currentmoney < Teams[j].gmoney():
            Teams[j + 1] = Teams[j]
            j -= 1
        Teams[j + 1] = currentteam
def insertionc():
    
    for i in range(len(cars2)):
        currentmoney = cars2[i].grating()
        currentteam = cars2[i]
        j = i - 1
        while j >= 0 and currentmoney < cars2[j].grating():
            cars2[j + 1] = cars2[j]
            j -= 1
        cars2[j + 1] = currentteam
def createcars():
    for i in range(len(Teams)):
        nice = car(Teams[i].gname())
        nice.carset(Teams[i].gexperience(), Teams[i].gmoney(), Teams[i].gsponsors())
        cars.append(nice)
        cars2.append(nice)
insertion()
createcars()
insertionc()
def bestteam():
    print('Teams Ranked ~')
    for i in range(len(Teams)):
        print('Position',i + 1,':',Teams[i])
def fastestcar():
    print('Cars Ranked ~')
    for i in range(len(cars)):
        print('Position',i + 1,':',cars2[i])
def get_menu_choice():
    while True:
        choice = int(input("Input a number from the list(0-3)."))
        if 0 <= choice <= 3:
            return choice
            break
        else:
            print("Input a valid option.")
def display_menu():
    print("1. List Best Teams and Cars.")
    print("2. List the stats of the team and their car")
    print("3. Show Tracks")
    print("0. Save and Quit.")
    print()
    print("Select an option from the menu above")
def mainmenu():
    print("This is the race management program.")
    print()
    while True:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            bestteam()
            fastestcar()
        elif option == 2:
            teamno = int(input("Input the number from the list corresponding to team you wish to check:"))
            if 0 < teamno < 9:
                print(Teams[teamno-1].stats())
                print(cars[teamno-1].stats())
        elif option == 3:
            for i in range(len(Tracks)):
                print(Tracks[i].stats())
        elif option == 0:
            break
    print()
    print("Thanks for using the Model management program.")
mainmenu()








    