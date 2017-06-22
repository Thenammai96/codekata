n=int(input("enter a number"))
i=0
c=0
while n>0:
    q=int(n/10)
    r=int(n%10)
    n=q
    c+=1
print(c)
