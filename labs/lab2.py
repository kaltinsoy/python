print("Enter i, j, k!")
x = int(input())
y = int(input())
z = int(input())

i, j, k = 0, 0, 0
while i <= x:
    j = 0
    while j <= y:
        k = 0
        while k <= z:
            print(i, j, k)
            k += 1
        j += 1
    i += 1

dna_sequence = "AGCTTAGCGAATCGGCTA"

nucleoid_count = {nucleoid: dna_sequence.count(nucleoid) for nucleoid in "AGCT"}

for nucleoid, count in nucleoid_count.items():
    print(f"{nucleoid} count: {count}")

listTuples = [(3, 9), (5, 2), (8, 1), (6, 7), (10, 4)]

sortedTuples = sorted(listTuples, key = lambda x: abs(x[0]-x[1]))
print(sortedTuples)

strings = ['red', 'indigo', 'green', 'magenta', 'yellow', 'white', 'lavender', 'orange']
sortedStrings = sorted(strings, key = lambda x: len(set(x)))
print(sortedStrings)

data = [("Dennis Ritchie", 1941), 
 ("Alan Kay", 1940), 
 ("John Backus", 1924), 
 ("Ada Lovelace", 1815), 
 ("John von Neumann", 1903),
 ("James Gosling", 1955)]

sortedData = sorted(data, key=lambda x: x[0].split()[-1], reverse=True)
print(sortedData)