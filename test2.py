def count_odd_digits(number):
    oddNumber = {"1","3","5","7","9"}
    count = 0

    while number > 0:
        digit = number % 10
        if str(digit) in oddNumber:
            count += 1
        number//= 10
    return count


    return print("Odd Number count:",a)

number = int(input("Enter Number"))
print(count_odd_digits(number))
