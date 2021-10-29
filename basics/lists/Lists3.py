# list1 = ["apple", "cherry", "banana", "mango", "kiwi"]
# list2 = list1   #copying the list1 into list2
# print(list2)

# #here we delete any element from any of the list, it will delete from both the lists....
# #because list2 contains the reference of the list1... 
# list1.pop()
# print(list1)
# print(list2)

# list2.pop()
# print(list2)
# print(list1)



# here list3 is actually copy into list4,
# so operations on their respective list will not occur in other list...
#  
# list3 = ["apple", "cherry", "banana", "mango", "kiwi"]
# 
# list4 = list3.copy()
# 
# print(list4)
# print(list3)

# list3.pop()
# print(list3)
# print(list4)

# list4.pop(2)
# print(list4)
# print(list3)



x = [1, 2, 3]
y = ["a", "b", "c"]
z = x + y
print(z)

# orr we can do this by : 
x.extend(y)
print(x)  #y is added into x...


















