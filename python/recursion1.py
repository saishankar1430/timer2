def f(n):
    if n == 0:
        return
    print(n, end=" ")
    f(n-1)
    print(n,end=" ")
f(4)