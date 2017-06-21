n=int(input("enter first number"))
m=int(input("enter second number"))
o=int(input("enter third number"))
if m>n and m>o:
    print(m)
    print(" is larger")
elif n>m and n>o:
    print(n)
    print(" is larger")
else:
    print(o)
    print(" is larger")
