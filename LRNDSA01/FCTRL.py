# cook your dish here
t = int(input())
while(t):
    n = int(input())
    z = 0
    while(n//5):
        z = z + n//5
        n = n//5
    print(z)
    t=t-1