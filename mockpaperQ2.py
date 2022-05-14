




class Team:
    def __init__(self,teamname, p1, p2, p3 ,p4 ,p5, ranking):
        self.__teamname = teamname #STRING
        self.__player1 = p1 #STRING
        self.__player2 = p2 #STRING
        self.__player3 = p3 #STRING
        self.__player4 = p4 #STRING
        self.__player5 = p5 #STRING
        self.__ranking = ranking #INTEGER
    def getdetails(self):
        print("Team name:", self.__teamname)
        print("Player 1:", self.__player1)
        print("Player 2:", self.__player2)
        print("Player 3:", self.__player3)
        print("Player 4:", self.__player4)
        print("Player 5:", self.__player5)
        print("Team ranking:", self.__ranking)
    def getranking(self):
        return (self.__ranking)
    def getteamname(self):
        return (self.__teamname)
#Question 2b
def ranker(textualranking):
    num = 0
    for i in range(len(textualranking)):
        if textualranking[i] == " ":
            space = i + 1
    if textualranking[:5] == "Bronze":
        num = num+4
    if textualranking[:5] == "Silver":
        num = num+8
    if textualranking[:4] == "Gold":
        num = num+12
    if textualranking[:8] == "Platinum":
        num = num+16
    if textualranking[:7] == "Diamond":
        num = num+20
    if textualranking[:6] == "Master":
        num = num+24
    if textualranking[:11] == "Grandmaster":
        num = num+28
    if textualranking[:10] == "Challenger":
        num = num+32
    if textualranking[space:] == "I":
        num = num + 1
    if textualranking[space:] == "II":
        num = num + 2
    if textualranking[space:] == "III":
        num = num + 3
    if textualranking[space:] == "IV":
        num = num + 4
    return num
print(ranker("Grandmaster II"))

arrayTeam = []
#Question 2c
def split(current):
    for i in range(len(current)):
        if current[i] == ",":
            splt = i
            return(splt)
def readData():
    try:
        with open("Gamers.txt","r") as f:
            for i in range(16):
                nameholder = []
                numholder = []
                for i in range(5):
                    current = f.readline().strip()
                    username = current[:split(current)]
                    pranking = current[split(current) + 1:]
                    prankingno = ranker(pranking)
                    nameholder.append(username)
                    numholder.append(prankingno)
                tranking = 0
                for i in range(len(numholder)):
                    tranking = tranking + int(numholder[i])
                teamname = (str(nameholder[0][0]+nameholder[1][0]+nameholder[2][0]+nameholder[3][0]+nameholder[4][0]))
                arrayTeam.append(Team(teamname,nameholder[0],nameholder[1],nameholder[2],nameholder[3],nameholder[4],tranking))
    except OSError:
        print("file not found")


readData()

#Question 2d
print(arrayTeam[15].getdetails())
def insertion(arrayTeam):
    for i in range(len(arrayTeam)):
        currentrank = arrayTeam[i].getranking()
        currentteam = arrayTeam[i]
        j = i - 1
        while j >= 0 and currentrank < arrayTeam[j].getranking():
            arrayTeam[j + 1] = arrayTeam[j]
            j -= 1
        arrayTeam[j + 1] = currentteam

insertion(arrayTeam)

print(arrayTeam[15].getdetails())
print("first bracket")
for i in range(0,7):
    print(arrayTeam[i].getteamname())
print("second bracket")
for i in range(7,11):
    print(arrayTeam[i].getteamname())
print("third bracket")
for i in range(11,14):
    print(arrayTeam[i].getteamname())
print("fourth bracket")
for i in range(14,16):
    print(arrayTeam[i].getteamname())