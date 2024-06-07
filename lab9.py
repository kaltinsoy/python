
# class FilterIterator:
#     def __init__(self, iterable, func):
#         self.iterable = iterable
#         self.func = func
#         self.index = 0
#     def __iter__(self):
#         # student code
#         return self
#     def __next__(self):
#         while self.index < len(self.iterable):
#             item = self.iterable[self.index]
#             self.index += 1
#             return item
#         raise StopIteration

# def is_positive(x):
#     return x > 0

# numbers = [6, 5, -2, 8, -9, -3, 7]
# filtered_iterator = FilterIterator(numbers, is_positive)

# for num in filtered_iterator:
#     print(num)

def evens(numero):
    for x in range(numero+1):
        if x % 35 == 0:
            yield x

numero = int(input("Enter numero!"))
for i in evens(numero):
    print(i)