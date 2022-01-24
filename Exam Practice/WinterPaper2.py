import os


class Picture():
    def __init__(self, Description, Width, Height, Colour):
        self.__Description = Description
        self.__Width = Width
        self.__Height = Height
        self.__Colour = Colour
    def __repr__(self):
        return self.__Description
    def GetDescription(self):
        return self.__Description
    def GetHeight(self):
        return self.__Width
    def GetWidth(self):
        return self.__Height
    def GetColour(self):
        return self.__Colour
    def SetDescription(self, Description):
        self.__Description = Description
    def SetHeight(self, Height):
        self.__Height = Height
    def SetWidth(self, Width):
        self.__Width = Width
    def SetColour(self, Colour):
        self.__Colour = Colour
    def GetAll(self):
        print("Description:" ,self.__Description)
        print("Width:" ,self.__Width)
        print("Height:" ,self.__Height)
        print("Colour:" ,self.__Colour)




Array = [Picture('','','','') for i in range(1,100)]
def ReadData():
    lines = 0
    try:
        with open("Pictures.txt","r") as f:
            for line in f:
                f.readline()
                lines = lines + 1
            new = lines*2
            f.seek(0)
            for i in range(0, new):
                Array[i].SetDescription(f.readline())
                Array[i].SetWidth((f.readline())[0:2])
                Array[i].SetHeight((f.readline())[0:2])
                Array[i].SetColour(f.readline())
            print ("Number of pictures written:", new)
    except OSError:
        print("Sorry, could not find the file. Make sure it is in the correct directory. The current directory is",os.getcwd())

ReadData()


print("Input criteria for image search:")
colour = input("Input Colour:")
width = input("Input max width:")
height = input("Input max height:")
colour = colour.lower()
if int(width) >= 100:
    width = "99"
if int(height) >= 100:
    height = "99"
for i in range(len(Array)):
    if colour == (Array[i].GetColour())[0:len(colour)]:
        if height > (Array[i].GetHeight())[0:len(height)]:
            if width > (Array[i].GetWidth()[0:len(width)]):
                print(Array[i].GetAll())


