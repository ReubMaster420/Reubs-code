Array = [1,2,4,6,7,8,19,29,36,74]
find = int(input("Enter a number to find in the list:"))
found = False
for i in range(len(Array)):
    if Array[i] == find:
        found = True
if(found):
    print("The number",find,"was found")
else:
    print("The number", find,"was not found in the array.")
    

