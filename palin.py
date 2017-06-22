n=int(input("etner a number"))
m=n
s=0
while n>0:
        r=int(n%10)
        n=int(n/10)
        s=s*10+r
if s==m:
    print("it is palindrome")
else:
    print("it  is not a palindrome")
