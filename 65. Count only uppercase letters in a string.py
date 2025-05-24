#65. Count only uppercase letters in a string.
s="koTEswRAraO"
count=0

i=0
while i<len(s):
    if s[i].isupper():
        count+=1
    i+=1
print(count)