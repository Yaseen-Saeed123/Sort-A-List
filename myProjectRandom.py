# Objective: Order a list ascendingly or descendingly
import random as r

# Function for adding ones
def add_one(no):
    key = str(no)
    value = myDict[key]
    value += 1
    myDict[key] = value

print("-"*100)
# Step 1: Get number of elements
while True:
    try:
        print("How many elements to sort?")
        elementNo = int(input("=> ").strip())
        break
    except:
        print("Invalid input")

print("-"*100)

# Step 2: Generate a random list and append each value to number to the number of ones
myList = []
myDict = {}
digits = len(str(abs(elementNo)))
base = 10
while len(myList) < elementNo:
    var = r.random() * (base ** digits)
    var = int(var)
    while var in myList:
        var = r.random() * (base ** digits)
        var = int(var)
    myList.append(var)
    key = str(var)
    myDict[key] = 0

print(f"My List before ordering: {myList}")
print("-"*100)

# Step 3: Compare each number with all other numbers
for _ in myList:
    index = myList.index(_)
    while index < elementNo:
        try:
            i = myList[index + 1]
            if _ > i:
                add_one(_)
            elif _ < i:
                add_one(i)
            index += 1
        except IndexError:
            break

# Step 4: Organise the dict and order the numbers
ordered_list = [0 for i in range(elementNo)]
for key in myDict.keys():
    try:
        value = myDict[key]
        ordered_list[value] = int(key)
    except IndexError:
        break

print(f"My List after ordering: {ordered_list}")
print("-"*100)