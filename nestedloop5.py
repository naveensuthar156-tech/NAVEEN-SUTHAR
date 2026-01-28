# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5 

i=1
while i<=5:
    j=5
    while j>=i:
        print(j,end=' ')
        j=j-1
    print()
    i=i+1