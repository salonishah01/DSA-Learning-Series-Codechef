# cook your dish here
t = int(input())
while(t):
    n = int(input())
    s = input()
    chanceA = chanceB = n
    sumA = sumB = 0
    for i in range(0, 2 * n ):
        if(i % 2 == 0):
            if(s[i] == '1'):
                sumA = sumA + 1 
            chanceA  = chanceA - 1 
        else:
            if(s[i] == '1'):
                sumB  = sumB + 1 
            chanceB  = chanceB - 1 
        if(sumA > sumB + chanceB):
            print(i+1)
            break
        elif(sumB > sumA + chanceA):
            print(i+1)
            break
        elif(sumA == sumB and i == 2 * n - 1):
            print(i + 1)
            break
    t = t - 1 
            
        
                