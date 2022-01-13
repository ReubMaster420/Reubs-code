LinkedList = []
class Node():
    def __init__(self, Data, Pointer):
        self.__Data = Data
        self.__Pointer = Pointer
    def pointer(self):
        return self.__Pointer
    def data(self):
        return self.__Data
StartPointer = 0

LinkedList.append(Node('A', 1))
LinkedList.append(Node('B', 2))
LinkedList.append(Node('C', 3))
LinkedList.append(Node('D', -1))

def FindValue(Value):
    CurrentPointer = StartPointer
    while CurrentPointer != -1 and LinkedList[CurrentPointer].data() != Value:
        CurrentPointer = LinkedList[CurrentPointer].pointer()
    if LinkedList[CurrentPointer].data() == Value:
        return (CurrentPointer)
    else:
        return (-1)

print(FindValue('H'))
