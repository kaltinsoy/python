def sum_lesser(lst, integ):
    newList = []
    
    for num in lst:
        if num < integ:
            newList.append(num)

    return newList

lst = [21,38,15,49,32,18,44]
integ = 29
print(sum_lesser(lst, integ))