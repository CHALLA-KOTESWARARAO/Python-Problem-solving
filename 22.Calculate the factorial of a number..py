#22.Calculate the factorial of a number.
a=5
fact=1
for i in range(a,0,-1): #fact,a+1
    fact*=i
print(fact)