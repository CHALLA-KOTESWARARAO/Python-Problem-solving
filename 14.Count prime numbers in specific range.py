#14. Count the number of prime numbers in a specific range.
num=int(input("Enter the range of number to count prime numbers:"))
count=0
a=[]
for i in range(2,num+1):
    prime=True
    for j in range(2,(i//2)+1):
        if i%j==0:
            prime=False
            break
    if prime==True:
        count+=1
        a.append(i)
print("the count of prime numbers:",count)
print(a)


