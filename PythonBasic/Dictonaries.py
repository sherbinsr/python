

students ={
           1 : "ram",
           2 : "polard",
           3  : "steve",
           4  : "edward"
}

# prints all dictionary elements
print(students)

# print all the keys
print(students.keys())

# prints all values
print(students.values())

# update the element in dict
students.update({1:"bob"});
print(students)

# update function can also used for adding new elements in set
students.update({5:"Joy"})
print(students)

# delete  function in dict
students.pop(5)
print(students)

# clears dict
students.clear()
print(students)