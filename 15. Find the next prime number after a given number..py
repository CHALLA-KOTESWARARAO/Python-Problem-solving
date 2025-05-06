#15. Find the next prime number after a given number.
num=int(input("enter a number:"))
for i in range(2,num+10):
    prime=True
    for j in range(2,(i//2)+1):
        if i%j==0:
            prime=False
            break
    if prime==True:
        if i>num:
            print(i)
            break