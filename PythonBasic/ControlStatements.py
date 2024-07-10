# break statement
while True:
    name =input("what is your name")
    if name !="":
        break

# continue statement

for i in range (10):
    if i % 2 ==0:
        continue
    else:
        print(i)

# pass statement

for i in range (10):
    if i == 2:
        pass
    else:
        print(i)
