#24. Check if a number is a perfect square.
#perfect sqaure nums 4(2*2),9(3*3),16(4*4)
num=25
p=False
for i in range(2,(num//2)+1):
    if i*i==num:
        p=True
        break
if p==True:
    print(num,"is perfect number")
else:
    print(num,"is not perfect number")
