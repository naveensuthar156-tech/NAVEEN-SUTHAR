a=int(input("enter your number:-"))
b=int(input("enter your number:-"))
c=int(input("enter your number:-"))
if(a>b):
    if(a>c):
        print("a is big")
    else:
        print("b is big")
elif(b>c):
    print("b is big")
else:
    print("c is big")
