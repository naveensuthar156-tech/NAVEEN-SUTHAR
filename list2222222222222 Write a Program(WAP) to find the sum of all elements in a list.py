list=[]
n=int(input("enter your value:---"))
for i in range(1,n+19):
    value=int(input("enter your value----"))
    list.append(value)
print(list)
sum=0
for item in list:
    sum=sum+item
print("sum all list iteam:--",sum)
                       