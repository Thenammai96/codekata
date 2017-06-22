a=int(input("enter start range"))
c=0
m=a
while a>0:
    r=int(a%10)
    a=int(a/10)
    c=c+r*r*r
if m==c:
    print("it is amstrong number")
else:
    print("it is not amstrong number")
