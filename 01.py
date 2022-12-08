n = int(input("Give me n: "))

for i in range(1, n+1):
    for j in range(1, n+1):
        print(j, end = '')
        if(j==i):
            print()
            break