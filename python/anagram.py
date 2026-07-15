def checkAnangram(s1, s2):
    if len(s1) != len(s2):
        return False
    hasharray = [0]*26
    for i in range(0, len(s1)):
        hasharray[ord(s1[i])- ord('a')] += 1
        hasharray[ord(s2[i])- ord('a')] -= 1
    for i in hasharray:
        if i != 0:
            return False
    return True

s1 = "listen"
s2 = "silent"

print(checkAnangram(s1,s2))