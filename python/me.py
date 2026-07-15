a = [1,12,3,4,5,28,6,7,8,9,10]
max = a[0]
for i in a:
    if i > max and i < 8:
        max = i
print(max)

min = 1000
for i in a:
    if i < min and i > 20:
        min = i
print(min)