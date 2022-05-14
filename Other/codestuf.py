def dequeue(item):
   global queuelength, frontpointer, item
   if queuelength == 0:
        print("Queue is empty, cannot dequeue")
   else:
       item = queue[frontpointer]
       if frontpointer == len(queue) -1:
           frontpointer = 0
        else:
            frontpointer = frontpointer + 1
    queuelength = queuelength -1
