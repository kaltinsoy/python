import re

handle = open("test.txt", "r")
sum=0
count=0

for line in handle:
	line = line.rstrip()
	number = re.findall('[0-9]+', line)

	for n in number:

		count+=1
		sum+=int(n)

print("Sum", sum)
print("Count", count)
print("avarage :", sum//count)
