class TreasureChest:
    def __init__(self, question, answer, points):
        self.__question = question
        self.__answer = answer
        self.__points = points
    def getdeets(self):
        print("Question:",self.__question)
        print("Answer:",self.__answer)
        print("Points:",self.__points)
    def __repr__(self):
        return self.__question
    def getquestion(self):
        return self.__question
    def checkAnswer(self,userans):
        if self.__answer == userans:
            return True
        else:
            return False
    def getPoints(self,attempts):
        if attempts == 1:
            return self.__points
        if attempts == 2:
            return int(int(self.__points)/2)
        if attempts == 3 or attempts == 4:
            return int(int(self.__points)/4)
        if attempts > 4:
            return 0


arrayTreasure = []
def readData():
    try:
        with open("TreasureChestData.txt","r") as f:
            for i in range(0,5):
                question = f.readline().strip()
                answer = int(f.readline().strip())
                points = int(f.readline().strip())
                arrayTreasure.append(TreasureChest(question,answer,points))
            f.close()
    except OSError:
        print("Could not find the file")

readData()
questselec = int(input("Enter a question number from 1 - 5:"))
print(arrayTreasure[questselec-1].getquestion())
attempts = 1
while True:
    ansinput = int(input("What the answer?:"))
    if arrayTreasure[questselec -1].checkAnswer(ansinput) == True:
        break
    if attempts > 4:
        break
    else:
        attempts = attempts +1
        print(attempts)
print(arrayTreasure[questselec-1].getPoints(attempts),"points")

