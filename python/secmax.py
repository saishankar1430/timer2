a = [5, 4, 3, 2, 1, 0, 10, 9, 8, 7, 6]
max = a[0]
secmax = -1
maxIndex = 0
sMaxindex = -1
for i in range(1, len(a)):
    if a[i] > max:
        secmax = max
        max = a[i]
        sMaxindex = maxIndex
        maxIndex = i
    elif a[i] > secmax and a[i] != max:
        secmax = a[i]
        sMaxindex = i
        
print("the secmax element is at index", i)
print("Maximum element is:", max)
print("Second maximum element is:", secmax)
