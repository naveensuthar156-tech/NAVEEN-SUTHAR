list=[["naveen",12,34,56,78,90],["dhanraj",45.67,78.90],["kumar",23,45,67,89,90],["sai",12,34,56],["ram",78,34,56,67]],[]
i=0
while i<len(list):
    j=0
    sum=0
    while j<len(list[i]):
        if j!=0:
            sum=sum+list[i][j]
        j=j+1
    print("total marks of",list[i][0],"is:",sum)
    i=i+1
####
