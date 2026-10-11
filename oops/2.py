# // create own data type by the help of class

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
    def __str__(self):
        return f"Student(Name: {self.name}, Age: {self.age})"

student1 = Student("Alice", 20)
student1.display()
# print(type(student1))  # <class '__main__.Student'>
# print(student1.name)  # Alice
# print(student1.age)   # 20

# # object 2

student2 = Student("Bob", 22)
print(student2)  # Student(Name: Bob, Age: 22)

class Team:
    def __init__(self, members):
        self.members = members
        
    def __len__(self):
        return len(self.members)

team = Team(["Alice", "Bob"])
print(len(team))  # Output: 2


class Score:
    def __init__(self, points):
        self.points = points
        
    def __add__(self, other):
        return Score(self.points + other.points)
        

    
a = Score(10)
b = Score(20)   

result = a + b
print(result.points)  # Output: 30