a = [int(i) for i in input().split()]
c = 0 
for j in range(len(a)):
    if len(a) <= 1:
        print(a[0])
        break
    if j != len(a) - 1:
        c = (a[j-1]) + (a[j+1]) 
    elif j == len(a) - 1:
        c = (a[j-1]) + (a[0])
    print(c, end=' ')
