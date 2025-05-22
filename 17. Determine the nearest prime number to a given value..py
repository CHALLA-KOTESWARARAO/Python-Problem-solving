# # #17. Determine the nearest prime number to a given value

n=13
a=[]

for i in range(n-5,n+5):
    prime=1
    for j in range(2,i//2+1):
        if i%j==0:
            prime=0
            break
    if prime:
        a.append(i)
print(a)

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
