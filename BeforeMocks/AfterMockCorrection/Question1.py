sample = ["75/3050","30/4815","460/4670","250/1500","160/1909","330/1330","210/1551"]
num = []
denom = []
fractions=[]

def numbersplit(arr):
    for i in range(len(sample)):
        char = ""
        flag = True
        for x in range(len(sample[i])):
            if sample[i][x] == "/":
                flag = False
                denom.append(int(sample[i][x+1:]))
            if flag == True:
                char = char+sample[i][x] 
        num.append(int(char))

def recursive(num,denom):
    if denom/num == denom//num:
        return denom//num
    else:
        recursive(num,denom/num)

numbersplit(sample)
print("Numerator:",num)
print("Denominator:",denom)

for i in range(len(num)):
    fractions.append(recursive(num[i],denom[i]))

print(fractions)
