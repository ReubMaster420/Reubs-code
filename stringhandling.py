ringgit = "RM129"
print(f"{ringgit}")


numcol1 = [1,5,8]
numcol2 = [3,7,13]
numcol3 = [12,15,9]

print("Binary:")
for i in range(3):
    print(f"{numcol1[i]:b} {numcol2[i]:b} {numcol3[i]:b}")

print("Hexadecimal:")
for i in range(3):
    print(f"{numcol1[i]:>x} {numcol2[i]:>x} {numcol3[i]:>x}")
# Note the order here. >15 and then .2f which is 2 decimal places

print("Decimal:")
for i in range(3):
    print(f"{numcol1[i]:d} {numcol2[i]:d} {numcol3[i]:d}")
