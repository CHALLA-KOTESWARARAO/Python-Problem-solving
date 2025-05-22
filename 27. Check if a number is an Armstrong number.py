#27. Check if a number is an Armstrong number.
'''
153 = 153(1**3 + 5**3 +3**3) power is 3 because of 3 digits
1634=1634(1**4 + 6**4 +3**4 + 4**4 )
'''
num=1634
sum=0
st=str(num)
length=len(st)
for i in st:
    sum+=int(i)**length
print(sum)
if num==sum:
    print(num,"is armstrong number")
else:
    print(num,"is not armstrong number")