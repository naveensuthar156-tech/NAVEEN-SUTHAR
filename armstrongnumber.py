### number that is equal to the sum of its digits raised to a power, where the power is the total number of digits.
n=int(input("enter your value----"))
sum=0
x=n
while n>0:
    a=n%10
    sum=sum+a*a*a
    n=int(n/10)
if x==sum:
    print("armstrong")
else:
    print("not armstrong ")



print("\n")
#
sure='y'
while sure=='y':
    n=int(input("enter your value----"))
    sum=0
    x=n
    while n>0:
        a=n%10
        sum=sum+a*a*a
        n=int(n/10)
    if x==sum:
        print("armstrong")
    else:
        print("not armstrong ")
sure=input("do you want to continue?y/n____:--")