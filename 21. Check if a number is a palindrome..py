#21. Check if a number is a palindrome.
num=5004
st=str(num)
palin=""
for i in range(len(st)-1,-1,-1):
    palin+=st[i]
if st==palin:
    print(f'{num} is palindrome')
else:
    print(f'{num} is not palindrome')