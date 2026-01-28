n = int(input("Enter a number: "))
i=2
while i<n:
    if n%i==0:
        break
    i=i+1
if n == i:
    print("Prime number")




print("\n")
#

n = 1
while n <= 1000:
    i = 2
    while i < n:
        if n % i == 0:
            break
        i = i + 1

    if i == n:
        print(n)

    n = n + 1
