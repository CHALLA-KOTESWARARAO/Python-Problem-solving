#13. Check if a number is a prime number.
num=int(input("enter number to check prime or not:"))

if num>=1:
    p=1
    for i in range(2,(num//2)+1):
        if num%i==0:
            p=0
            break
else:
    print("invalid input and enter number which is greater than 1")

if p==1:
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")

#Using While
num=int(input("enter number to check prime or not:"))

if num>=2:
    p=True
    i=2
    while i<=(num//2):

        if num%i==0:
           p=False
           break
        i+=1
else:
    print("invalid input and enter number which is greater than 1")

if p==True:
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")
