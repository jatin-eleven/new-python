set1 = {"apple", "banana", "Mango"}
set2 = {"Kiwi", "orange"}

#adds the set1 and set2 into set3
set3 = set1.union(set2)
print(set3)

#adds the set2 into set1
set1.update(set2)
print(set1)


new_set = set(("peach", "guwava"))
print(new_set)


#sets contains only unique elements...
list1 = [1, 1, 1, 2, 3, 2, 1, 4, 5, 6, 6, 2]
print(set(list1)) 

