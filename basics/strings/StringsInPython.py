strings = "hello world"
name = input("enter name : ")
print(name)

print("char is : " + strings[6])
print(strings[1:7])#prints the char form 1 to (7-1)
print("char is : " + strings[-11])
print(len(strings))
print(len("jatin suthar"))

var1 = "   helloo   "
print(var1.strip()) #remove whitespace at the starting and ending

var2 = "JATIN Suthar"
print(var2.lower())
print(var2.upper())

var3 = "hello world"
print(var3.replace("ll", "  namaste  "))

print(var3.split())  #split the word at white space
print(var3.split("o"))  #split the word at '0'

check = "ll" in var3
print(check)

check = "C" not in var3
print(check)

a = "Hello"
b = "World"
print(a + " " + b)

zz = " hello"

