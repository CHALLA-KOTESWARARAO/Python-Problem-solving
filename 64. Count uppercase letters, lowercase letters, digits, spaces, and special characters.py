#64. Count uppercase letters, lowercase letters, digits, spaces, and special characters.

s="KOTEswararo@#$%^&123  456  85"
upper=0
lower=0
digits=0
space=0
specialchars=0
i=0

while i<len(s):
    if s[i].islower():
        lower+=1
    elif s[i].isupper():
        upper+=1
    elif s[i].isdigit():
        digits+=1
    elif s[i].isspace():
        space+=1
    else:
        specialchars+=1
    i+=1
print(f'lower:{lower} upper:{upper} digits:{digits} space:{space} specialchars:{specialchars}')

