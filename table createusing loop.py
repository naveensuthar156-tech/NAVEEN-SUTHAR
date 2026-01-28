n=int(input("Enter the number for which you want to create a table: "))
for i in range(1,11):
    print(n,"*",i,"=",n*i)
    i=i+1
    
    
    
    
##
sure=0
while sure==0:
    n=int(input("Enter the number for which you want to create a table: "))
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
        i=i+1
    sure=int(input("Do you want to continue? Press 0 for Yes and 1 for No: "))