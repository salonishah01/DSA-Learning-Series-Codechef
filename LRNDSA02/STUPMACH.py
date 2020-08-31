# cook your dish here
t = int(input())
while(t):
    n = int(input())
    x = list(map(int, input().split()))
    s = m = 0
    for i in range(len(x)):
        if(i == 0):
            m = x[i]
        else:
            m = min(m, x[i])
        s = s + m
    print(s)
    t = t - 1
            