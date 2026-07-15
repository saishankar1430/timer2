a = input("enter a statement of lower case characters which contains all characters: ")

len = len(a)
b = ""

for i in range(0, len):
    if 'a' <= a[i] <= 'z':
        b += chr(ord(a[i]) - 32)
    else :
        b += a[i]

print(b)

    
    
    
    