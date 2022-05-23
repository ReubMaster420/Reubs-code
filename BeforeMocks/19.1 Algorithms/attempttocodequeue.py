
frontofqueue=0
rearpointer=-1
queuefull = 8
queueLength = 0
queue = ([" " for i in range(8)])

def enqueue(data):
    global rearpointer
    global queueLength
    if queueLength < queuefull:
        if rearpointer < len(queue) -1:
            rearpointer = rearpointer +1
        else:
            rearpointer = 0
        queueLength = queueLength + 1
        queue[rearpointer] =data
    else:
        print("Queue is full")


def dequeue():
    global frontofqueue
    global rearpointer
    global item
    global queueLength
    if queueLength == 0:
        print("list is empty, nothing to remove")
    else:
        item = queue[frontofqueue]
        queue[frontofqueue] = " "
        if frontofqueue == len(queue) -1:
            frontofqueue = 0
        else:
            frontofqueue = frontofqueue +1
    queueLength = queueLength - 1

print(queue)
enqueue("Brian Flu")
enqueue("Jihad")
print(queue)
enqueue("Aidsddn")
dequeue()
print(queue)
