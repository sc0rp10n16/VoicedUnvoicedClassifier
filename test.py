test = int(input())

for i in range(test):
    s = True
    n = int(input())
    a = list(map(int, input().split()))
    
    for f in range(n):
        for u in range(f,n):
            if a[f] == a[u]:
                print("NO")
                s = False
                break
        if s == False:
            break
    if s == True:
        print("YES")
        

for zero in range(times):
    lom=int(input())
    aen=True
    wom=list(map(int,input().split()))
    for one in range(lom):
        for two in range(one,lom):
            if wom[one]==wom[two]:
                print("NO")
                aen=False
                break
        if aen==False:
            break
    
    if aen==True:
        print("YES")