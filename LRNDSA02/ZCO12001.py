
N = int(input()) 
arr = [0]+list(map(int, input().split()))     
stack = [] 
start_end = []
j = 1
Max = 0
stacklen = 0
while j < len(arr):
    if arr[j] == 1: 
        stack.append(j)
        stacklen += 1
        
    else: 
        start_end.append((stack[-1], j))
        stack.pop()
        stacklen -= 1
 
    if stacklen > Max: 
        Max = stacklen
        pos = j
 
    
 
    j += 1
 
p = 0
for i in start_end:
    if i[1] - i[0] > p: 
        p = i[1] - i[0] + 1
        pos2 = i[0]
 
print(Max, pos, p, pos2)