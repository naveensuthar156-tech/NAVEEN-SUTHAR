n=int(input("enter your value:-"))
fact=1
while n>=0:
    fact=fact*n
    n=n-1
    print("factorial:-",fact)





print("\n")
#
sure='y'
while sure=='y':
    n=int(input("enter your value:-"))
    fact=1
    while n>0:
        fact=fact*n
        n=n-1
    print("factorial:-",fact)
    sure=input("do you want to continue?(y/n):")