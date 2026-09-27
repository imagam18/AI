print("Agam Saxena"); print("Hello World"); print("This is a test")

# Adding a new line
print("This is a new line added to the code",end =" ")
print("This is the second part of the new line added to the code")


"""
x = str(input("Enter your name: "))
print("Hello, " + x + "! Welcome to the world of Python programming.")
print(type(x ))  # This will print the type of the variable x, which is <class 'str'>
"""

# Good abbrevation technique

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# there are three types of casing techniques used in python
# 1. Camel Case
print("Camel Case: myVariableName")
# 2. Pascal Case
print("Pascal Case: MyVariableName")
# 3. Snake Case
print("Snake Case: my_variable_name")

# Assigning multiple values to multiple variables
a, b, c = "Orange", "Banana", "Cherry"
print(a)
print(b)
print(c)

x = y =z = "Orange"
print(x)
print(y)
print(z)

# USE of global keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

