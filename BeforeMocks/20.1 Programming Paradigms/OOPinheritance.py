#oop1
class employee:
    def __init__(self, name, staffno):
        self.__name = name #__ represent data hiding
        self.__staffno = staffno
    def showDetails(self):
        print("Employee Name:",self.__name)
        print("Employee Numbert:",self.__staffno)
    
#subclass1

class parttime(employee):
    def __init__(self, name, staffno):
        employee.__init__(self, name, staffno)
        self.__fullTimeStaff = False
        self.__hoursworked = 0
    def getHoursWorked(self):
        return self.__hoursworked

#subclass2

class fulltime(employee):
    def __init__(self, name, staffno):
        employee.__init__(self, name, staffno)
        self.__fullTimeStaff = True
        self.__yearlySalary = 0
    def getYearlySalary(self):
        return self.__yearlySalary

permanentstaff = fulltime("Eric Jones", 72)
permanentstaff.showDetails()
tempstaff = parttime("Alice hue", 1017)
tempstaff.showDetails()
