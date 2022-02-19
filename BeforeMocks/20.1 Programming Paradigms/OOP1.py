class employee:
    def __init__(self, name, staffno):
        self.__name = name #__ represent data hiding
        self.__staffno = staffno
    def showDetails(self):
        print("Employee Name:",self.__name)
        print("Employee Numbert:",self.__staffno)
myStaff = employee("Eric Jones",72)
myStaff.showDetails()
    