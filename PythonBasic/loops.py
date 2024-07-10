
# while loop
x =1;
while x != 10:
    print(x)
    x+=1

# for loop
for i in range (10):
    print(i)
for i in range (10,50):  # (start,stop)
    print(i)
for i in range (10,50,2): # (start,stop,step)
    print(i)

#nested loop
for i in range (10):
    for j in range(10):
        print(i,j)