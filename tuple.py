mytuple = ("apple", "banana", "cherry")
print(mytuple)

# basic feature of tuple is that it is immutable, meaning you cannot change its values after it has been created.

thistuple = ()
print(type(thistuple))  # This will print <class 'tuple'>

# Tuple constructor 
thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(thistuple)

# assesing same as the list, string and other data types
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])  # This will print the second item in the tuple, which is 'banana'


# Loops
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
    
# Change the tuple value

x = ("apple", "banana", "cherry")
y = list(x)  # Convert the tuple to a list
y[1] = "kiwi"  # Change the second item in the list
x = tuple(y)  # Convert the list back to a tuple
print(x)  # This will print ('apple', 'kiwi', 'cherry')


# Adding tuple to the tuple

thisTuple = ("apple", "banana", "cherry")
y = ("orange",)
thisTuple += y  # Add the new tuple to the existing tuple
print(thisTuple)  # This will print ('apple', 'banana', 'cherry',

# unpacking of the tuple

fruits = ("apple", "banana", "cherry")
green, yellow, red = fruits  # Unpack the tuple into three variables
print(green)  # This will print 'apple'
print(yellow)  # This will print 'banana'
print(red)  # This will print 'cherry'


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# methods of tuple
# count() method returns the number of times a specified value occurs in a tuple.
thistuple = (1, 3, 7, 8, 7,5, 4, 6, 8, 5)
print(thistuple.count(5))  # This will print 2, as 5 occurs twice in the tuple
# index() method returns the index of the first occurrence of a specified value in a tuple.
thistuple = (1, 3, 7, 8, 7,5, 4, 6, 8, 5)
print(thistuple.index(8))  # This will print 3, as the first
