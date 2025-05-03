#13. Check if a number is a prime number.
num=int(input("enter number to check prime or not:"))
p=1
for i in range(2,(num//2)+1):
    if num%i==0:
        p=0
        break

if p==1:
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")
# num=int(input("enter number to check prime or not:"))
# i=2
# p=True
# while i<=num-1:
#     if num%i==0:
#         p=False
#         break
#     i+=1
# if p==True:
#     print(f"{num} is prime number")
# else:
#     print(f"{num} is not prime number")
