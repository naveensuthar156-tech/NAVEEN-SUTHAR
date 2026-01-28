n=int(input("enter your value:--"))
x=n
rev=0
while n>0:
    a=n%10
    rev=rev*10+a
    n=int(n/10)
if x==rev:
    print(" this is palindrom")
else:
    print(" not palindrom")




print("\n")
#
sure='y'
while sure=='y':
    n=int(input("enter your value:--"))
    x=n
    rev=0
    while n>0:
         a=n%10
         rev=rev*10+a
         n=int(n/10)
if x==rev:
     print(" this is palindrom")
else:
     print(" not palindrom")



