str="qwertyuioplkjhgfdsazxcvbn"
for char in str:
    print(char)
    if(char=='g'):
        break
    print(char)
else:
    print("END")