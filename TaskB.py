
import pickle

class TaskB:
    def __init__(self, line, Finish=False):
        self.SylPoint = line
        self.Finish = Finish
    def getter(self):
        return self.Finish
    def setter(self):
        Finish = str(input("Enter t or f:"))
        if Finish == 't':
            self.Finish = True
        if Finish == 'f':
            self.Finish = False
X = TaskB("Hello")
with open("191.pickle","wb") as y:
    with open("newpractical.txt","r") as f:
        for line in f:
            if line[0:4] == "19.1":
                print(line[5::].strip())
                X.setter()
                X.getter()
                pickle.dump(TaskB(str(line[5::].strip()),X.Finish),y)
   
with open("191.pickle","rb") as z:
    for i in range(19):
        test = pickle.load(z)
        print(test.SylPoint,":",test.Finish)






