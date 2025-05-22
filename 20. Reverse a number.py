#20. Reverse a number.
num=50502
s=str(num)
rev_num=""
for i in range(len(s)-1,-1,-1):
    rev_num+=s[i]
print(rev_num)

#method2
#reverse a number without converting string