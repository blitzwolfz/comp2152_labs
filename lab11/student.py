# student.py

from person import Person

class Student(Person):
    def __init__(self, name, age, height, major):
        super().__init__(name, age, height)
        self.major = major
        print("This time it's a Student object")


# === Test code ===

# Create an instance of Person
person = Person("Mark", 20, 6)

# Print the public attribute 
print(person.public_prop)

# Try printing the private name property directly 
try:
    print(person.__name)
except AttributeError as e:
    print(f"Error: {e}")

# Access name using property getter and setter
print(person.name)     
person.name = "Anna"   
print(person.name)     

# Create an instance of Student
student = Student("Maria", 22, 6, "Computer Science")
