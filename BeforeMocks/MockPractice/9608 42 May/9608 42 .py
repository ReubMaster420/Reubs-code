#1b
from pickle import FALSE


#

#2
class CustomerRecord:
    def __init__(self, Username,Password):
        self.__username = Username
        self.__password = Password
    def Username(self):
        return self.__username

CustomerLogIn = (CustomerRecord("","") for i in range(1,3000))

#2bi
def SearchHashTale(SearchUser):
    Index = 0
    count = 0
    while (CustomerLogIn[Index].Username != SearchUser) and (CustomerLogIn[Index].Username != "") and (count < 2999):
        Index = Index + 1
        count = count + 1
        if Index > 2999:
            index = 0
    if CustomerLogIn[Index].Username == SearchUser:
        return Index
    else:
        return(-1)

#3b
def Palindrome(word):
    word= word.lower()
    length = len(word)
    if length < 2:
        return True
    elif word[0] == word[length- 1]:
        return Palindrome(word[1: length - 1])
    else:
        return False

print(Palindrome('tenet'))

#3c 
def FindPower(Basenumber,exponent):
    if exponent == 0:
        return(1)
    if exponent == 1:
        return(Basenumber)
    else:
        return(Basenumber*(FindPower(Basenumber,exponent-1)))
 
import random
#7
class Character:
    def __init__(self, name):
        self.__name = name
        self.__skill = 0
        self.__health = 50
        self.__shield = random.randint(1,25)
    def getskill(self):
        return self.__skill
    def setskill(self, value):
        if value < 10 or value > 25:
            print("this is not valid")
            return(-1)
        else:
            if self.__skill + value >= 200:
                return(0)
            else:
                self.__Skill = self.__Skill + value 
                return(1)

