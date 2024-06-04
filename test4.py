inventory = {
'laptop': 50,
'headphones': 25,
'blender': 30,
'microwave': 40,
'desk lamps': 20
}

sortedInventory = dict(sorted(inventory.items()))

print("Sorted Inventory: ")

for product, quantity in sortedInventory.items():
    print(f"{product}: {quantity}")


list1 = [1, 3, 5, 6, 9]
list2 = [2, 3, 4, 10, 1]

zipped = zip(list1, list2)

comp = ['<' if x < y else '>' if x > y else '=' for x,y in zipped]
print(comp)

names = ["Ali", "Ayse", "Fatma"]
studentID = [22231, 22312, 22314]
grade = [90, 80, 70]

zipped = zip(names,studentID,grade)

for name, studentIDs, grades in zipped:
    print(f"Name: {name}, Student ID: {studentIDs}, grade: {grades}")

def filter_numbers(*args, **kwargs):
    newList = []
    for arg in args:
        for key, value in kwargs.items():
            if value == 0:
                value = 1
            if arg % value == 0:
                newList.append(arg)
    print(newList)

filter_numbers(10, 20, 30, 40, divisor1=2, divisor2=3, divisor3=5)

