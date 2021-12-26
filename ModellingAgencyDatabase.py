import os
Models = []
parts = []
class ModelData:
    def __init__(self, firstname, lastname, gender, Mobile, Email ,Age, Country, Dresssize, otheragencies):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__gender = gender
        self.__mobile = Mobile
        self.__email = Email
        self.__age = int(Age)
        self.__country = Country
        self.__dresssize = int(Dresssize)
        self.__otheragencies = otheragencies
    def __repr__(self):
        return self.__firstname
    def showdetails(self):
        print("First name:" ,self.__firstname)
        print("Last name:" ,self.__lastname)
        print("Gender:" ,self.__gender)
        print("Mobile:" ,self.__mobile)
        print("Email:" ,self.__email)
        print("Age:" ,self.__age)
        print("Country:" ,self.__country)
        print("Dress size:" ,self.__dresssize)
        print("Other agencies:" ,self.__otheragencies)
    def showname(self):
        return self.__firstname
    def showcountry(self):
        return self.__country
    def showemail(self):
        return self.__email
    def getter(self, dressupper, dresslower, ageupper, agelower, country):
        if self.__dresssize >= dresslower and self.__dresssize <= dressupper and self.__age >= agelower and self.__age <= ageupper and self.__country == country:
            return self
        else:
            pass
try:
    with open("ModellingAgencyData.txt","r") as whole_file:
        for line in whole_file:
            parts = line.split(",")
            Models.append(ModelData(*parts))
except OSError:
        print("Sorry, could not find the file. Make sure it is in the correct directory. The current directory is",os.getcwd())
def setter(firstname, lastname, gender, Mobile, Email ,Age, Country, Dresssize, otheragencies):
    if Country in ('Brunei', 'Myanmar', 'Cambodia', 'Timor-Leste', 'Indonesia', 'Laos', 'Malaysia', 'Philippines', 'Singapore', 'Thailand', 'Vietnam'):
        if gender == ('Male') and 46 <= Dresssize <= 58:
            new = ModelData(firstname, lastname, gender, Mobile, Email ,Age, Country, Dresssize, otheragencies)
            Models.append(new)
        if gender in ('Female','Non-Binary') and 32 <= Dresssize <= 48:
            new = ModelData(firstname, lastname, gender, Mobile, Email ,Age, Country, Dresssize, otheragencies)
            Models.append(new)
    else:
        print("Invalid parameters")
def insertion():
    countrylist = []
    for i in range(len(Models)):
        new = Models[i].showcountry()
        countrylist.append(new)
    for i in range(len(countrylist)):
        currentvalue = countrylist[i]
        currentmodel = Models[i]
        j = i - 1
        while j >= 0 and currentvalue < countrylist[j]:
            countrylist[j + 1] = countrylist[j]
            Models[j + 1] = Models[j]
            j -= 1
        countrylist[j + 1] = currentvalue
        Models[j + 1] = currentmodel
insertion()
def mail():
    with open("ModellingAgencyEMAILS.txt","w") as newfile:
        for i in range(len(Models)):
            line = Models[i].showemail()+ " Hi "+ Models[i].showname() +" There is a client who is interested in your profile. Please could you make an appointment at the agency for your briefing. Kind regards Sasha Jonas\n"
            newfile.write(line)

def get_menu_choice():
    while True:
        choice = int(input("Input a number from the list(0-3)."))
        if 0 <= choice <= 3:
            return choice
            break
        else:
            print("Input a valid option.")
def display_menu():
    print("1. Add models to the system.")
    print("2. Select models and display details")
    print("3. create emailer")
    print("0. Save and Quit.")
    print()
    print("Select an option from the menu above")
def mainmenu():
    print("This is the Model management program.")
    print()
    while True:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            inputm = input("Put in the Model parameters as (firstname, lastname, gender, Mobile, Email ,Age, Country, Dresssize, otheragencies):")
            setter(inputm)
            print()
        elif option == 2:
            for i in range(len(Models)):
                print(Models[i].showname())
            find = input("Type the name of a model you want to find out more about:")
            for i in range(len(Models)):
                if find == Models[i].showname():
                    print(Models[i].showdetails())
            print()
        elif option == 3:
            mail()
        elif option == 0:
            break
    print()
    print("Thanks for using the Model management program.")
mainmenu()








    




