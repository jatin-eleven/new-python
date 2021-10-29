list3 = [000, 111, 222, 333, 444, 555]
print(len(list3))

list3.append("apple")  #add "apple" at the end of the list...
print(list3)

list3.insert(2, "orange")  #insert at the specific index..
list3.insert(4, "kiwi")
print(list3)

print(list3.pop()) #pop the last element in the list...

print(list3.pop(2))

#or we can use "del" keyword for delete the elements/vars....
del list3[3]
print(list3)

del list3  #deleted the whole-list deleting the variable called list3 ...


list4 = [111, 222, 333, 444, 555]
list4.clear() #clear all the elements present in the list...
print(list4)
