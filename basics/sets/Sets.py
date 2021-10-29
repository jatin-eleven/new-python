
#In SETS we cannot change the items present, but we can add items....
# sets contains only unique elements :- don't repeat elements...
#it is Unordered and immutable.....

set1 = {"apple", "mango", "cherry"}
print(set1)

for items in set1 : #prints elements unordered manner..... 
    print(items)
    print("-----")

print("mango" in set1)
print("kiwi" in set1)

print()

# adding items in the sets...
set1.add('orange')
print(set1)
print()
# #adding more than one items at a time...
set1.update(["kiwi", "grapes"]) 
print(set1)
print(len(set1))

#deleting elements from the lists...
set1.remove("apple")
print(set1)
print(len(set1))

set1.discard("cherry")
print(set1)
print(len(set1))

set1.pop()
print(set1)

set1.clear()
print(set1)


               