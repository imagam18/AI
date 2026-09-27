# String

x = "Hello, World!"
print(x[1])  # This will print the character at index 1 (which is 'e')
print(x[2:5])  # This will print the characters from index 2 to 4 (which is 'llo')
print(len(x))  # This will print the length of the string (which is 13)
print(x.strip())  # This will print the string with leading and trailing whitespace removed
print(x.lower())  # This will print the string in lowercase
print(x.upper())  # This will print the string in uppercase
print(x.replace("H", "J"))  # This will replace the character 'H' with 'J'
print(x.split(","))  # This will split the string at the comma and return a list


for x in "banana":
  print(x)  # This will print each character in the string "banana" on a new line

MyString = "Hello, World!"
if "Hello" in MyString:
  print("Yes, 'Hello' is present in the string")  # This will print if 'Hello' is found in MyString
# not in
if "Hello" not in MyString:
  print("No, 'Hello' is not present in the string")  # This will print if 'Hello' is not found in MyString  
  
age = 36
txt = f"My name is John, I am {age}"
print(txt)



# BOOL
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))