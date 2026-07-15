a = [1,12,3,4,5,28,6,7,8,9,10]
i = 0
j = len(a) - 1

while i<j:
    a[i], a[j] = a[j], a[i]
    i+=1
    j-=1
    
print(a)