#Question 1
import time 
start = time.time()
fractions = ["75/3050","30/4815","460/4670","250/1500","160/1909","330/1330","210/1551"]
new = []
top = []
bottom = []
def half():
    for i in range(len(fractions)):
        for x in range(len(fractions[i])):
            if fractions[i][x] =="/":
                top.append(int(fractions[i][:x]))
                bottom.append(int(fractions[i][x+1:]))
                break
half()

print("Before recursive function:",fractions)
def simplify(top,bottom):
    i = 0
    while i != 24:
        for i in range(2,25):
            if top%i == 0 and bottom%i == 0:
                top = top/i
                bottom = bottom/i
                simplify(top,bottom)
                break
    return(str(int(top))+"/"+str(int(bottom)))

    
for i in range(len(top)):
    fractions[i] = simplify(top[i],bottom[i])
print("After recursive function",fractions)

#Question 1b
end = time.time()
print("Time taken was",end - start)

#Question 1c
decimals = []
for i in range(len(top)):
    decimals.append(top[i]/bottom[i])

dict ={}
for i in range(len(top)):
    dict[fractions[i]] = decimals[i]
print(dict)