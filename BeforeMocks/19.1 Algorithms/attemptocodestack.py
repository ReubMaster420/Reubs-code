stack = []
lengthofstack= 0
stackfull = 8
stack = [" " for i in range(8)]

def push(data):
    global lengthofstack
    if lengthofstack == stackfull:
        print("Stack is full cannot push")
    else:
        stack[lengthofstack]=(data)
        lengthofstack = lengthofstack + 1
 
def pop():
    global lengthofstack
    if lengthofstack == 0:
        print("Operation unavailable, stack it empty")
    else:
        stack[lengthofstack-1] = " "
        lengthofstack = lengthofstack-1

def printstack():
    for i in range(lengthofstack):
        j = (lengthofstack-1) - i
        print(stack[j])

push("John")
print(stack)
push("Chris")
push("Abdullah")
print(stack)
pop()
print(stack)
pop()
push("Inshallah")
print(stack)