def rev_range(n):
    while(n>0):
        yield n-1
        n-=1

for i  in rev_range(4):
    print(i)