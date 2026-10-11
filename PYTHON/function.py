def _main_function():
    print("hello function")
    
_main_function()

def _temp_Fah_Cel(fahrenheeit):
    return(fahrenheeit-32)*5/9

print(_temp_Fah_Cel(55))


def _greet(name):
    print("hello Mr /Mrs:" + name)

_greet("Agam")
_greet("Smrita")


def _args_func(*args):
    for x in args:
        print("Hello: "+ x)

_args_func("agam","smrita")

print("Hello World")
def my_function(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")
        
my_function("Hello", "Alice", "Bob", "Charlie")

def _kwargs_fun(**kwargs):
    for x,y in kwargs.items():
        print(x,y)
_kwargs_fun(name ='Agam',age = 30 , city ="Banglore")

def _unpack_func(a ,b ,c):
    return a + b +c
number = [ 1,2,3]
print(_unpack_func(*number))


# Combining *args and **kwargs in a function
def _combined_func(title,*args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
    
_combined_func("My Function", "Alice","Alice", "Bob", name="Alice", age=30)


# scope of functions

def my_function():
    x = 10  # Local variable
    print("Inside the function, x =", x)
my_function()


def _outer_function():
    x = 300
    
    def _inner_function():
        print(x)
    _inner_function()

_outer_function()


x = 10  # Global variable

def my_function():
    print("Inside the function, x =", x)  # Accessing the global variable
    
my_function()

print("Outside the function, x =", x)  # Accessing the global variable outside the function


def my_function():
    global x  # Declare x as a global variable
    x = 20  # Modify the global variable
    print("Inside the function, x =", x)
my_function()
print("Outside the function, x =", x)  # Accessing the modified global variable outside the function

# LEGB Rule

x = "global x"
def outer_function():
    x = "enclosing x"
    
    def inner_function():
        x = "local x"
        print("Inside the inner function, x =", x)  # Accessing the local variable
        
    inner_function()
    print("Outside the function, x =", x)  # Accessing the enclosing variable
outer_function()
print("Global x:", x)  # Accessing the global variable