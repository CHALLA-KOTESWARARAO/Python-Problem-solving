#26. Identify if a number is a strong number.
'''
145 is strong numbers 
1!+4!+5!=1+24+120 sum of each digit factorial of num == num
=145
'''
num=145
k=str(num)
sum=0
for i in range(len(k)):
    l=1
    for j in range(1,int(k[i])+1):
        l*=j
    sum+=l
if sum==num:
    print(num,"is strong number")
else:
    print(num,"is not strong number")
        

    
