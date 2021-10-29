list1 = ["apple", 2, "banana", "cherry", 7, "orange"]
print(list1[2])

print(list1[-1])
print(list1[-3])

print(list1[0:5])    #prints the element from 0 to (5-1) 
print(list1[-5:-2])  #prints the element from -5 to (-2-1) = -3



list2 = [111, 222, 333, 444, 555]
print(list2[0:5])  #prints all the values present in the list...
print(list2[:])    #prints all the values present in the list...

print(list2[:3])   #prints values from starting to index 3...
print(list2[1:])   #prints values from index 1 to end...




names = ['Amir', 'Bear', 'Charlton', 'Daman']
print(names[-1][-1])
# Explanation
# This operation is called negative indexing in python. At first we have selected "Daman" and then     # selected element at index -1 which is "n".
