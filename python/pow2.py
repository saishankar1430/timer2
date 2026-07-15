def f(a,b):
    if b == 0:
        return 1
    if b % 2 == 0:
        k = f(a,b // 2)
        return k * k
    else: 
        k = f(a, (b -1 ) / 2)
        return a * k * k
print(f(2,10))