


RootPointer = -1
FreeNode=0
ArrayNodes=[[0 for x in range(3)]for Y in range(20)]


#b)
def AddNode(NodeData):
    global RootPointer,FreeNode,ArrayNodes
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0]= -1
        ArrayNodes[FreeNode][1]= NodeData
        ArrayNodes[FreeNode][2]= -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while Placed == False:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode = FreeNode + 1
    else:
        print("Tree is full")
    
def PrintAll():
    print("LeftPointer             Data             RightPointer")
    for i in range(len(ArrayNodes)):
        print(ArrayNodes[i][0],"                    ",ArrayNodes[i][1],"                ",ArrayNodes[i][2])



AddNode(10)
AddNode(5)
AddNode(15)
AddNode(8)
AddNode(12)
AddNode(6)
AddNode(20)
AddNode(11)
AddNode(9)
AddNode(4)
PrintAll()

def InOrder(RootNode):
    if ArrayNodes[RootNode][0] != -1:
        InOrder(ArrayNodes[RootNode][0])
    print(str(ArrayNodes[RootNode][1]))
    if ArrayNodes[RootNode][2] != -1:
        InOrder(ArrayNodes[RootNode][2]) 
InOrder(0)