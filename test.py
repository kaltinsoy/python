def is_long(string):
    if len(string) > 10:
        print("Very Long!")
    else:
        print("Short!")

def shorter(string0,string1):
    if len(string0) > len(string1):
        print(string0," is the longer!")
    else:
        print(string1," is the longer!")

def later(string0,string1):
    return print(max(string0,string1))

string = input("Enter string!")
is_long(string)
string0 = input("Enter str0")
string1 = input("Enter str1")
shorter(string0,string1)
later(string0,string1)