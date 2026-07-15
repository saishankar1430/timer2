char = input("enter a character: ")

if 'a' <= char <= 'z':
    print("it is a lower case character")
elif 'A' <= char <= 'Z':
    print("it is a uppercase character")
elif '0' <= char <= '9':
    print("it is a digit")
else :
    print("it is a special character")