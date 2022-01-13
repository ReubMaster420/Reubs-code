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

Array = [Picture for i in range(1,100)]
