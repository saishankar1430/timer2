def romanDecimal(c):
    if c == "I":
        return 1
    elif c == "X":
        return 10
    elif c == "V":
        return 5
    elif c == "L":
        return 50
    elif c == "C":
        return 100
    elif c == "M":
        return 1000
    else:
        return 500
    
roman = "XLIVDVLM"
n = len(roman)
i = 0
val = 0

while i < n:
    if i == n - 1:
        val += romanDecimal(roman[i])
        break
    elif romanDecimal(roman[i]) < romanDecimal(roman[i+1]):
        val += romanDecimal(roman[i + 1]) - romanDecimal(roman[i])
        i += 2
    else:
        val += romanDecimal(roman[i])
        i += 1
print(val) 