#25. Verify if a number is a sunny number.
# if numbers adds with 1 which has to be perfect square
#15+1==(4*4),24+1==(5*5)
num=15
p=False
for i in range(2,(num//2)+2):
    if i*i==(num+1):
        p=True
        break
if p==True:
    print(num,"is a sunny number")
else:
    print(num,"is not sunny number")
