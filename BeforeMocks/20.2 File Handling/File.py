
import pickle

class student:
    def __init__(self):
        self.name = ""
        self.registerNumber = 0
        self.dateofbirth= 0
        self.fullTime = True
studentRecord = student()
studenFile = open('students.DAT','w+b')
print("Enter student details")
studentRecord.name = input("Enter name")
studentRecord.registerNumber =  int(input("reg no"))
pickle.dump(studentRecord, studenFile) #puts record into file
studenFile.close()
studenFile = open('students.DAT','rb')
studentRecord = pickle.load(studenFile)
print('all the shag')
studenFile.close()