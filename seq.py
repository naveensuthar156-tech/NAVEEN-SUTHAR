seq=range(18)
print(seq[0])
print(seq[1])
print(seq[2])       
print(seq[3])
print(seq[4])
print(seq[5])
print(seq[6])
print(seq[7])
print(seq[8])
print(seq[9])
print(seq[10])
print(seq[11])
print(seq[12])
print(seq[13])
print(seq[14])  
print(seq[15])
print(seq[16])
print(seq[17])
i=0
sum=0
while i<18:
    sum=sum+seq[i]
    i+=1
print("Sum is:",sum)


####
i=0
fab=0
n1=0
n2=1
sum=0
while i<18:
    if i<=1:
        fab=i
    else:
        fab=n1+n2
        n1=n2
        n2=fab
    print(fab)
    sum=sum+fab
    i+=1
print("Fabonicci of 18th term is:",fab)
print("Sum of Fabonicci series is:",sum)



#####################
i=0
sum=0
for i in range(0,18):
    sum=sum+seq[i]  
    i
print("Sum using for loop is:",sum)



####
i=0
fab=0
n1=0        
n2=1
sum=0
for i in range(0,18):
    if i<=1:
        fab=i
    else:
        fab=n1+n2
        n1=n2
        n2=fab
    print(fab)
    sum=sum+fab
    i=i+1
print("Fabonicci of 18th term using for loop is:",fab)
print("Sum of Fabonicci series using for loop is:",sum)
