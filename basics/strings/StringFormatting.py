num = 5
text = "there are {} apples"
formatted_text = text.format(num)
print(formatted_text)

print(f"there are {num} apples") 


print("We are the co-called \"Vikings\" from the north")

print(isinstance(num, int)) #check the instance of the variable...


print("___________________________________________")


marks_python = 98
marks_cpp = 94
marks_java = 96

text1 = "I got {} marks in python, {} marks in cpp and {} marks in Java"

print(text1.format(marks_python, marks_cpp, marks_java))


print("___________________________________________")


marks_kotlin = 98
marks_Swift = 94
marks_javaScript = 96

text2 = "I got {2} marks in javaScript, {0} marks in Kotlin and {1} marks in Swift" 
#here the numbers are in curly braces are the indexes acc. to which values are assigned by variables

print(text2.format(marks_kotlin, marks_Swift, marks_javaScript))
# index               {0}           {1}          {2}


print("___________________________________________")


text3 = "i have {device} which has {software} software."
print(text3.format(device = "MacBook", software = "MacOS"))  # Same Output

print(text3.format(software = "MacOS", device = "MacBook"))  # Same Output


print("___________________________________________")


marks_py = 96
text4 =  f"I scored {marks_py} marks in Python"
print(text4)












