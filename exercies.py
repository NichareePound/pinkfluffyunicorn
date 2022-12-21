# Create an empty list called teamlist
teamlist = []

# Use a for loop to append 11 names to the list
for i in range(11):
    name = input("Enter a name: ")
    teamlist.append(name)

# Traverse the list and print out each name
for name in teamlist:
    print(name)
