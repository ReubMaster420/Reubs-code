import os
Models = []
parts = []
clist = []
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
    def showname(self):
        return self.__firstname
    def showcountry(self):
        return self.__country

try:
    with open("ModellingAgencyData.txt","r") as whole_file:
        for line in whole_file:
            parts = line.split(",")
            Models.append(ModelData(*parts))
except OSError:
        print("Sorry, could not find the file. Make sure it is in the correct directory. The current directory is",os.getcwd())

for i in range(len(Models)):
    clist.append(Models[i].showcountry())

print(clist)
def insertion():
    for i in range(len(Models)):
        currentcountry = Models[i].showcountry()
        currentmodel = Models[i]
        j = i - 1
        while j >= 0 and currentcountry < Models[j].showcountry():
            Models[j + 1] = Models[j]
            j -= 1
        Models[j + 1] = currentmodel
insertion()
clist = []
for i in range(len(Models)):
    clist.append(Models[i].showcountry())

print(clist)