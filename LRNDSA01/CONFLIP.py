# cook your dish here
t = int(input())
while(t):
    g = int(input())
    while(g):
        I, N, Q = input().split()
        I = int(I)
        N = int(N)
        Q = int(Q)
        if(N % 2 == 0):
            print(N//2)
        else:
            if(I == Q):
                print((N-1)//2)
            else:
                print((N+1)//2)
        g = g-1
    t = t-1