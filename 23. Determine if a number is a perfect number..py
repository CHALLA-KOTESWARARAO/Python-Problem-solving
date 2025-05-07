#23. Determine if a number is a perfect number.
#A perfect number is a positive integer that is equal to the sum of its proper positive divisors, excluding the number itself.
#Ex:(6) Its divisors (excluding 6 itself): 1, 2, 3|Sum: 1 + 2 + 3 = 6

num=28
lis=[]
for i in range(1,(num//2)+1):
    if num%i==0:
        lis.append(i)
l=sum(lis)
# l=0
# for i in lis:
#     l+=i
print("sum:",l)
if l==num:
    print("it is perfect number")
else:
    print("it is not perfect number")

