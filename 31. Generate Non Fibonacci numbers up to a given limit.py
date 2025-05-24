#31. Generate Non Fibonacci numbers up to a given limit.
i=0
j=1
n=10
non=0
while i<n:
    c=i+j
    i=j
    j=c
    non+=1
    if non!=i and non!=j:
        print(non)

