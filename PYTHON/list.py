thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print("the length of the list is: ",end="")
print(len(thislist))


# The list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets4
print("Thats the list constructor")
print(thislist)


if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
else:
  print("No, 'apple' is not in the fruits list")
  
  
# list insert() function
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print("Position 1, 'orange' is inserted in the list")


# append()function insert the element at the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print("The element 'orange' is added at the end of the list")
print(thislist)

# extend() function is used to add the elements of a list (or any iterable), to the end of the current list.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print("The elements of the list 'tropical' are added to the end of the list 'thislist'")
print(thislist)

#remove() function is used to remove the specified item from the list.
thislist = ["apple", "banana", "cherry"]
print("The element 'banana' is removed from the list")
thislist.remove("banana")
print(thislist)

# pop() function removes the specified index, (or the last item if index is not specified)
thislist = ["apple", "banana", "cherry"]
print("The last element of the list is removed")
thislist.pop(1)
print(thislist)


# Loop list items

thislist = ["apple", "banana", "cherry"]
print("This shows the list items using for loop")
for x in thislist:
    print(x)
    
# Range is used to loop through a set of code a specified number of times
thislist = ["apple", "banana", "cherry"]
print("This shows the range of the list")
for i in range(len(thislist)):
    print(thislist[i])

# While loop is used to execute a set of statements as long as a condition is true.
thislist = ["apple", "banana", "cherry"]
print("This shows the while loop of the list")
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
    

# list Comprehnesion 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
print("This shows the new list with items containing 'a':")
print(newlist)

# newlist = [expression for item in iterable if condition ==    True]

newlist = [x.upper() for x in fruits]
print("This shows the new list with all items in upper case:")
print(newlist)  


# sort()

fruits.sort()
print("This shows the sorted list:")
print(fruits)   

# Desending order
fruits.sort(reverse = True)
print("This shows the sorted list in descending order:")
print(fruits)


def myfunc(n):
    return (n -500)

PerPBankAc = [1000, 500, 650, 802, 203]
PerPBankAc .sort(key = myfunc,reverse = None)
print("Health insurance money has been deducted and left over money is :")
print(PerPBankAc)

# Copying a list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print("This shows the copied list:")
print(mylist)


# joining the list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
print("This shows the joined list:")
print(list1 + list2)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print("This shows the joined list using extend() function:")    
print(list1)

# or we can use the append() function to join the list
list1.append(list2)
print("This shows the joined list using append() function:")
print(list1)
