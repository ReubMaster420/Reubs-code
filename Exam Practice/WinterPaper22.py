import os


class Picture():
    def __init__(self, Description, Width, Height, Colour):
        self.__Description = Description
        self.__Width = Width
        self.__Height = Height
        self.__Colour = Colour
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
print("HI")
Array = [Picture for i in range(1,100)]

def ReadData():
    lines = 0
    try:
        with open("Pictures.txt","r") as f:
            print("Opened")
            if f == " ":
                f.readline()
                lines = lines + 1
            print(lines)
            f.seek()
            #for i in range(lines/4):
             #   Array[i].SetDescription(f.readline())
               # Array[i].SetWidth(f.readline())
             #   Array[i].SetHeight(f.readline())
              #  Array[i].SetColour(f.readline())
    except OSError:
        print("Sorry, could not find the file. Make sure it is in the correct directory. The current directory is",os.getcwd())


ReadData()
