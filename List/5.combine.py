lim1 = int(input("Enter Limit of list 1:"))
lis1 = []
lis2 = []
lis3 = []

for i in range(lim1):
    lis1.append(int(input("Enter element:")))


lim2 = int(input("Enter Limit of list 2:"))

for i in range(lim2):
    lis2.append(int(input("Enter element:")))

print("Entered list 1:",lis1)
print("Entered list 2:",lis2)

for i in lis1:
    if i in lis2:
        lis3.append(i)
print("Output list:",lis3)