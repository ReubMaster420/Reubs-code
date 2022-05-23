from queue import Empty


class Picture:
    def __init__(self, Desc, Width, Height, Colour):
        self.__Desc = Desc #STRING
        self.__Width = Width #INTEGER
        self.__Height = Height #INTEGER
        self.__Colour = Colour #STRING
    
    def GetDescription(self):
        return self.__Desc
    def GetHeight(self):
        return self.__Height
    def GetWidth(self):
        return self.__Width
    def GetColour(self):
        return self.__Colour
    def SetDescription(self, newdesc):
        self.__Desc = newdesc

PictureArray = [Picture(None,None,None,None) for i in range(100)]




def ReadData():
    try:
        with open("Pictures.txt","r") as f:
            count = 0
            while count < 21:
                Desc = f.readline().strip()
                Width = f.readline().strip()
                Height = f.readline().strip()
                Colour = f.readline().strip()
                PictureArray[count]= Picture(Desc,Width,Height,Colour)
                count = count + 1
    except OSError:
        print("File not found")
    

ReadData()


colour = input("Please input the colour")
width = int(input("Enter the maximum width"))
height = int(input("The maximum height"))

for i in range(len(PictureArray)):
    if PictureArray[i].GetColour() == colour.lower() and int(PictureArray[i].GetWidth())< width and int(PictureArray[i].GetHeight())< height:
        print(PictureArray[i].GetDescription(),PictureArray[i].GetWidth(),PictureArray[i].GetHeight())