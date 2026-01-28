# add key
info={
      "name" : "naveen",
    "age" :  23,
    "add" :  "bikaner",
    "is_adult" : True,
    "phone no" : 234567890,
    "father name" :"rajesh suthar"
    
}
info["mother name"]="suman"
print(info)

# update key
info["age"]=24
print(info)

# delete key
del info["phone no"]
print(info)

# access all keys
print(info.keys())

# Access all values
print(info.values())
  
# access all items
print(info.items())

# loop through dictionary
for key , value in info.items():
    print("key is:", key ,",", "value is:", value)
    value=str(value)
    print("updated value is:", value) 
    info[key]=value
print(info)   
    



