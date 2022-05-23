class shape:
    def __init__(self):
        self.__areaValue= 0
        self.__perimeterValue = 0
    def area(self):
        print("Area ", self.__areaValue)
    def perimeter(self):
        print("Perimeter ", self.__perimeterValue)
class rectangle(shape):
    def __init__(self, length, breadth):
        shape.__init__(self)
        self.__length = length
        self.__breadth = breadth
    def area(self): #polymorphism is where methods are redefined for derived classes
        self.__areaValue= self.__length*self.__breadth
        print("Area ", self.__areaValue)
class circle(shape):
    def __init__(self, radius):
        shape.__init__(self)
        self.__radius = radius
    def area(self):
        self.__areaValue= 3.142*self.__radius*self.__radius
        print("Area ", self.__areaValue)
myCircle = circle(20)
myCircle.area()
myrec = rectangle(10,20)
myrec.area()


    
