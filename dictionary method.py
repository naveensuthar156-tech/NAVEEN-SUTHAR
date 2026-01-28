#keys
student={
      "name" : "naveen",
    "age" :  23,
    "add" :  "bikaner",
    "is_adult" : True,
    "phone no" : 234567890,
    "father name" :"rajesh suthar",
    "score" : {
        "hindi": 90,
        "english" : 89,
        "BEE" : 34
    }
}
print(len(student))
print(student.keys())
print(list(student.keys()))
print(tuple(student.keys()))


print()
#value
student={
      "name" : "naveen",
    "age" :  23,
    "add" :  "bikaner",
    "is_adult" : True,
    "phone no" : 234567890,
    "father name" :"rajesh suthar",
    "score" : {
        "hindi": 90,
        "english" : 89,
        "BEE" : 34
    }
}
print(len(student))
print(student.values())
print(list(student.values()))
print(tuple(student.values()))


print()
#iteam
student={
      "name" : "naveen",
    "age" :  23,
    "add" :  "bikaner",
    "is_adult" : True,
    "phone no" : 234567890,
    "father name" :"rajesh suthar",
    "score" : {
        "hindi": 90,
        "english" : 89,
        "BEE" : 34
    }
}
print(len(student))
print(student.items())
print(list(student.items()))
print(tuple(student.items()))


print()
#get
student={
      "name" : "naveen",
    "age" :  23,
    "add" :  "bikaner",
    "is_adult" : True,
    "phone no" : 234567890,
    "father name" :"rajesh suthar",
    "score" : {
        "hindi": 90,
        "english" : 89,
        "BEE" : 34
    }
}
print(len(student))
print(student.get("name"))
print(list(student.get("score")))
print(tuple(student.get("add")))



print()
#update
student={
      "name" : "naveen",
    "age" :  23,
    "add" :  "bikaner",
    "is_adult" : True,
    "phone no" : 234567890,
    "father name" :"rajesh suthar",
    "score" : {
        "hindi": 90,
        "english" : 89,
        "BEE" : 34
    }
}
student.update({"hight" : 5.9 })
print(student)

