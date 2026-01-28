n=int(input("enter your value:-"))
sum=0
while n>0:
    a=n%10
    sum=sum+a
    n=int(n/10)
print("sum of all digit",sum)




print("\n")
#
sure='y'
while sure=='y':
    n=int(input("enter your value:-"))
    sum=0
    while n>0:
        a=n%10
        sum=sum+a
        n=int(n/10)
    print("sum of all digit",sum)
    sure=input("continue?y/n:-")
