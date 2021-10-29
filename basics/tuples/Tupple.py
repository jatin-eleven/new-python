# Tupples are Ordered and immutable.....
# We cannot change the elements in the tuple after declaration...

tupple1 = ("apple", "mango", "orange", "melon", "kiwi", "banana")

for items in tupple1 : #print elements in Orederd manner...
    print(items)

print("_______________________________")


print(tupple1[0])
print(tupple1[1])
print(tupple1[-1])
print(tupple1[-2])


print("_______________________________")
#we cannot change the elements in tuple,
# so we convert the tuple into list -> change the element -> convert back into tuple....
list1 = list(tupple1)
list1[1] = "jimmy"
print(list1[:])

tupple1 = tuple(list1)
print(tupple1)

print("apple" in tupple1)
print("cherry" in tupple1)

print(len(tupple1))


print("_______________________________")


new_tup = ("apple")
print(type(new_tup))   #type is : String

# we have to leave a Comma(;) after an element
# (when there is single element in the tuple)
new_tup = ("apple",)
print(type(new_tup))   #type is : Tuple


tup1 = ("aaa", "bbb", "ccc")
tup2 = ("ddd", "eee", "fff")

tup3 = tup1 + tup2
print(tup3)

