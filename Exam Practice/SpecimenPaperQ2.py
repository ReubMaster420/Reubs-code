class HiddenBox:
    #__BoxName STRING
    #__Creator STRING
    #__DateHidden DATE
    #__GameLocation STRING
    #__LastFinds ARRAY
    #__Active BOOLEAN
    def __init__(self, BoxName, Creator, DateHidden, GameLocation):
        self.__BoxName = BoxName
        self.__Creator = Creator
        self.__DateHidden = DateHidden
        self.__GameLocation = GameLocation
        self.__LastFinds = [["" for j in range(0,2)]for i in range(0,10)]
        self.__Active = False
    def GetBoxName(self):
        return self.__BoxName
    def GetGameLocation(self):
        return self.__GameLocation

class PuzzleBox(HiddenBox):
    def __init__(self, NewBoxName, NewCreator, NewDateHidden, NewLocation, PuzzleText, Solution):
        HiddenBox.__init__(NewBoxName, NewCreator, NewDateHidden, NewLocation)
        self.__PuzzleText = PuzzleText
        self.__Solution = Solution

    
TheBoxes = (HiddenBox("","","","") for i in range(0,10000))

def NewBox():
    a = input("Input Box Name:")
    b = input("Input Creator Name:")
    c = input("Input Date Hidden:")
    d = input("Input Game Location:")
    TheBoxes.append(HiddenBox(a, b, c, d))




