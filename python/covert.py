a = input("enter a character")

if 'A' <= a <= 'Z':
    print(chr(ord(a)+ 32))
elif 'a' <= a <= 'z':
    print(chr(ord(a) - 32))
    