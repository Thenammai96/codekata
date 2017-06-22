a=int(input("enter start range"))
n=int(input("enter end number"))
c=0

for a in range (a,n):
    m=a
    while a>0:
        r=int(a%10)
        a=int(a/10)
        c=c+r*r*r
    if m==c:
        print(c)
    c=0
