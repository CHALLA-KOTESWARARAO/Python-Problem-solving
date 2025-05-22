#28. Generate Fibonacci numbers up to a given limit.
n=8
a=0
b=1
print(a,b,end=" ")
for i in range(1,n-1):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
#method-2

 