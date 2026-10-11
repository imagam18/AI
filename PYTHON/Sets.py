my_set = {
          "apple", "banana", "cherry"
          }
"""
A set is a collection which is unordered, unchangeable*, and unindexed.
"""
thisset = {
    "apple", "banana", "cherry", "apple"
    }

print(thisset)

# Zero and One consider True or False
thisset = {
    "apple", "banana", "cherry", False, True, 0,1
    }

print(thisset)

#Set Constrcutor

thisset = set((
    "apple", "banana", "cherry"
    ))
print(thisset)

# Accesing can't done by list bcz of unorderd so we use loop

thisset = {
    "apple","banana","cherry"
}
for x in thisset:
    print(x)
    
# Adding the sets items
thisset.add("Mango")
print(thisset)

# update() to get all data

tropical = {
    "Rassbery","ornage"
}
thisset.update(tropical)
print(thisset)

thisset = {"apple","banana","cherry"}
mylist = ["kiwi","orange"]

thisset.update(mylist)
print(thisset)
print(type(thisset))

#deleting from set has three main ways 

thisset = {"apple","banana","cherry"}
thisset.remove("banana")

print(thisset)


thisset.discard("cherry")
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# Python - Join Sets

# union() -> 

set_1 = {"a","b","c"}
set_2 = {1,2,3}

set_3 = set_1.union(set_2)
print(set_3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)


# join sets and the tuple

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#froxen sets

x = frozenset({"agam","manvi","Smrita"})
print(type(x))
print(x)