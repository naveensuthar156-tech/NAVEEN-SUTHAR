i=1
while i<=1000000:
    n=i
    x=n
    sum=0
    while n>0:
        a=n%10
        sum=sum+a*a*a
        n=int(n/10)
    if x==sum:
        print(x)
    i=i+1


