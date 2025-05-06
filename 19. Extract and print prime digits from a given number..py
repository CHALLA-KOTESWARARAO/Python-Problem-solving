#19. Extract and print prime digits from a given number.
num=2357114296
for i in str(num):
    if int(i)>=2:
        prime=True
        for j in range(2,(int(i)//2)+1):
            if int(i)%j==0:
                prime=False
                break
        if prime==True:
            print(i)




