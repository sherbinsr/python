

utensils = {"fork","spoon","knife"}
dishes  = {"bowl","plate","cup"}
print(utensils)

# printing set using loop
for i in utensils:
    print(i)

# add element
utensils.add("bottles")
print(utensils)

# removing element
utensils.remove("bottles")
print(utensils)


# concatnating  two sets
utensils.update(dishes)
print(utensils)

# concatnating  two sets
utensils.update(dishes)
print(utensils)

# clearing all element in set
utensils.clear()
print(utensils)