

cars =["vw","Bmw","Kia","tata"]

# prints the entire list
print(cars)

# print the value in index
print(cars[3])

# index replacing
cars[3] = "porsche"
print(cars[3])

# add new item
cars.append("Mercedes")
print(cars)

# remove a item
cars.remove("porsche")
print(cars)

# insert at index
cars.insert(1,"ford")
print(cars)

# printing list using loop
for i in cars:
    print(i)

# sorting list
cars.sort()
print(cars)

# clear list
cars.clear()
print(cars)
