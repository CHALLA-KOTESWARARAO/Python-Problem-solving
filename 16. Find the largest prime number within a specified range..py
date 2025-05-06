#16. Find the largest prime number within a specified range.
num=int(input("Enter the range of number to count prime numbers:"))
max=0
a=[]
for i in range(2,num+1):
    prime=True
    for j in range(2,(i//2)+1):
        if i%j==0:
            prime=False
            break
    if prime==True:
        if i>max:
            max=i
            a.append(i)
print(a)
print(max)
