#66. Count only lowercase letters in a string.
s="koTEswRAraO"
count=0

i=0
while i<len(s):
    if s[i].islower():
        count+=1
    i+=1
print(count)
