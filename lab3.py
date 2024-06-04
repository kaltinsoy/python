inventory = {
'laptop': 50,
'headphones': 25,
'blender': 30,
'microwave': 40,
'desk lamps': 20
}

lowLevel = 30

sortedNameInventory = dict(sorted(inventory.items()))
sortedQuantityInventory = dict(sorted(inventory.items(), key=lambda x: x[1]))
sortedLowInventory = dict(sorted({k: v for k, v in inventory.items() if v < lowLevel}.items(), key=lambda x: x[1]))

print(sortedNameInventory)
print(sortedQuantityInventory)
print(sortedLowInventory)

list1 = [1, 3, 5, 6, 9]
list2 = [2, 3, 4, 10, 1]

DataList = []

for num1, num2 in zip(list1,list2):
    if num1 > num2:
        DataList.append(">")
    elif num2 > num1:
        DataList.append("<")
    else:
        DataList.append("=")
print(DataList)

names = ["Ahmet", "Mehmet", "Mustafa", "Can", "Canan"]
studentIds = [123,231,321,415,235]
grades = [80,90,10,20,60]

ZippedList = zip(names, studentIds, grades)
for name, studentID, grade in ZippedList:
    print(f"Names: {name}, Student IDs: {studentID}, grades: {grade}")

def filterNums(*args, **kwargs):

    divisor = kwargs.get("divisor", 1)
    filteredNums = [num for num in args if num % divisor == 0]
    return filteredNums

print(filterNums(1, 2, 3, 4, 5, divisor=2))