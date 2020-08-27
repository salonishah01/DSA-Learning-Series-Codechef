# cook your dish here
t = int(input())
while(t):
    s = input()
    top = 0
    cnt = 0
    tmp = 0
    for i in range(len(s)):
        if(s[i] == '<'):
            top = top + 1 
        else:
            top = top -1
            if(top < 0):
                break
            tmp = tmp + 1 
            if(top == 0):
                cnt = tmp
    print(2*cnt)
    t = t-1