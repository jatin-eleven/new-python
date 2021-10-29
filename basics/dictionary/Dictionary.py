# dictionary : unordered data type....

dic1 = {
    "key1" : "value1",
    "key2" : "value2"
}

print(dic1)
print(dic1["key1"])

print("_____________________________________")

dic1 = {
    "brand" : "apple",
    "device" : "iphone",
    "software" : "ios"
}

dic1["device"] = "MacBook"
dic1["software"] = "MacOS"
print(dic1)

# for printing keys...
for keyName in dic1 :
    print(keyName)


print()


# for printing values...
for valName in dic1 :
    print(dic1[valName])
print()
# Alter (for values) :
for valName in dic1.values() :
    print(valName)


print()


# for printing both keys and values
for keyName, valName in dic1.items() : 
    print(keyName + " : " +  valName)


print()
print(dic1.items())
print(dic1.values())


print(len(dic1))

#for adding keys and values in dic.....
dic1["model"] = "Air"
dic1["color"] = "space gray"
for keyName, valName in dic1.items() : 
    print(keyName + " : " +  valName)


#for deleting items in the dic
dic1.pop("color")
print(dic1)

del dic1["model"]
print(dic1)

dic1.clear()
print(dic1)

#for copying one dic into another.....
dict1 = {
    'k1' : "a",    
    'k2' : "b",    
    'k3' : "c"    
}

dict2 = {
    'k4' : "d",    
    'k5' : "e"    
}

dict2 = dict1.copy()
print(dict2)

dict2 = dict(dict1)
print(dict2)

# using dict constructor.....
dict3 = dict(key1 = "aaa", key2 = "bbb", key3 = "ccc")
# here we use equal to (=) sign instead of colon(:) 
# and
# declare 'keys' without double qoutes ("")...
print(dict3)














