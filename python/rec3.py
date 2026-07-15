def f(n):
    if n == 0 or n == 1:
        return n+1
    return 2 * f(n-1) - 3 f(n - 2)

print(f(5))