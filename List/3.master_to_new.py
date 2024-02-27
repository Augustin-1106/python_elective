lim = int(input("Enter Limit:"))
lis = []
lis2 = []

for i in range(lim):
    lis.append(int(input("Enter element:")))

num = int(input("Enter a number:"))

print("Entered list:",lis)

for i in lis:
    if num > i:
        lis2.append(i)


print("New list:",lis2)