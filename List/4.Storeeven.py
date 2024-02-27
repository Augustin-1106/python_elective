lim = int(input("Enter Limit:"))
lis = []
lis2 = []

for i in range(lim):
    lis.append(int(input("Enter element:")))

print("Entered list:",lis)

for i in lis:
    if i%2 == 0:
        lis2.append(i)

lis2.sort()

print("New list:",lis2)