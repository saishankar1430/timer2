a = [1, 2, 3, 4, 5]
k = 4
while k != 0:
    temp = a[0] 
    for i in range(0, len(a) - 1):
        a[i] = a[i + 1]
    a[len(a) - 1] = temp
    k-= 1
print(a)
