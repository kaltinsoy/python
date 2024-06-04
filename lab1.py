def is_long(fname):
	if len(fname) < 10:
		return "short"
	else:
		return "long"

def shorter(short1, short2):
	if len(short1) > len(short2):
		return len(short2)
	else:
		return len(short1)


def later(late1, late2):
	if late1 > late2:
		return late1
	else:
		return late2


def count_odd_digits(numero):
	numero = int(numero)
	odds = [1,3,5,7,9]
	counter = 0

	while numero > 1:
		if numero%10 in odds:
			counter += 1
			numero = numero//10
		else:
			numero = numero//10

	return counter


def sum_lesser(lst, x):
	emptyList = []
	i = 0
	for num in lst:
		if num < x:
			emptyList.append(num)
			i = i + num

	print(emptyList, i)

print(is_long("pyhton"))
print(is_long("advanced python"))
print(shorter("purple", "gray"))
print(later("blue", "white"))
print(count_odd_digits(6754125))
sum_lesser([21,38,15,49,32,18,44], 29)
