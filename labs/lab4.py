def falling_iterative(n, k):
    result = 1
    i = 0
    while k > i:
        result = n * result
        n -= 1
        k -= 1
    return result

print(falling_iterative(7,5))

def falling_recursion(n,k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    else:
        return n * falling_recursion(n-1,k-1)

print(falling_recursion(10,2))

def merge(lst1, lst2):
    if not lst1:
        return lst2
    if not lst2:
        return lst1

    if lst1[0] < lst2[0]:
        return[lst1[0]] + merge(lst1[1:], lst2)
    else:
        return[lst2[0]] + merge(lst2[1:], lst1)
    
print(merge([1,3,5], [2,4,6]))
print(merge([], [2, 4, 6]))