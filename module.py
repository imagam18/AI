import random

print(random.randrange(1, 10)) ; print("This will print a random number between 1 and 10 (excluding 10)")
print(random.randint(1, 10))  ; print("This will print a random number between 1 and 10 (including both 1 and 10)")
print(random.choice(["apple", "banana", "cherry"]))  ; print("This will print a random item from the list")
print(random.sample(range(1, 100), 5))  ; print("This will print a list of 5 unique random numbers between 1 and 100")
print(random.uniform(1, 10))  ; print("This will print a random float number between 1 and 10")
print(random.shuffle([1, 2, 3, 4, 5]))  ; print("This will shuffle the list in place and return None")
print(random.getrandbits(8))  ; print("This will print a random integer with 8 random bits")
print(random.seed(10))  ; print("This will set the seed for the random number generator to 10")   

print(type())


import sys 

print(sys.version_info)
print(sys.version)
print(sys.platform)
print(sys.executable)