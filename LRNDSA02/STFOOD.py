# cook your dish here
import math
t = int(input())
while(t):
    n = int(input())
    prof = 0
    while(n):
        s,p,v = input().split()
        s = int(s)
        p =int(p)
        v = int(v)
        k = math.floor(p/(s+1))
        if(k*v > prof):
            prof = k* v
        n = n-1
    print(prof)
    t =t -1
        