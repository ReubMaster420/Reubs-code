import random
class Crop:
    def __init__(self, growthrate, lightneed, waterneed):
        self.__growth = 0
        self.__daysgrowing = 0
        self.__growthrate = growthrate
        self.__lightneed = lightneed
        self.__waterneed = waterneed
        self.__status = "Seed"
        self.__type = "Generic"
    def needs(self):
        print('Light needed: ', self.__lightneed)
        print('Water needed: ', self.__waterneed)
    def report(self):
        print('---------------------------------')
        print("Status Report.")
        print("Type        : ", self.__type)
        print("Status      : ", self.__status)
        print("Growth      : ", self.__growth)
        print("Days Growing: ",  self.__daysgrowing)
        print('---------------------------------')

class potato(Crop):
    def __init__(self):
        super().__init__(1,6,3)
        self.__type = "Potato"
    def potatorep(self):
        self.report()


potato_crop = potato()
print (potato.__status)