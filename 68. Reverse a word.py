#68. Reverse a word.
def rev(s):
    i=len(s)-1
    res=""
    while i>=0:
        res+=s[i]
        i-=1
    return res

s="python"
print(rev(s))