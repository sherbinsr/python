# formula behind the algorithm is  [start:stop:step]

city = "New york"

# creating substring
separating = city[0:3] # city[:3]
startStop = city[4:8]
funkyName = city[0:8:2]
reverseName = city[::-1]

print(separating)
print(startStop)
print(funkyName)
print(reverseName)

# create substring using slice()

website = "http.hilti.in"

sliceString = slice(0,8,2)
print(website[sliceString])