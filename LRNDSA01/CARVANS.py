# cook your dish here
t = int(input())
while(t):
    n = int(input())
    x = list(map(int, input().split()))
    cnt = 0
    for i in range(len(x)-1):
        if(x[i]<x[i+1]):
            cnt = cnt +1
            x[i+1] = x[i]
    print(n-cnt)
    t = t-1