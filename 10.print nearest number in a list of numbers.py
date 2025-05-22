#10.print nearest number in a list of numbers
a=[100,500,900,800]
n=849


b=a[len(a)-1]
c=0

for i in a:
    if i<n:
        j=n-i
        if j<b:
            b=j
            c=i
    elif i>n:
        j=i-n
        if j<b:
            b=j
            c=i
print(c)
