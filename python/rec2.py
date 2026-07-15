
def exponential(base, exp):
    if exp == 0:
        return 1
    else:
        return base * exponential(base, exp - 1)

print(exponential(2, 3))ṣ