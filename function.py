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


def _kwargs_fun(**kwargs):
    for x,y in kwargs.items():
        print(x,y)
_kwargs_fun(name ='Agam',age = 30 , city ="Banglore")

def _unpack_func(a ,b ,c):
    return a + b +c
number = [ 1,2,3]
print(_unpack_func(*number))