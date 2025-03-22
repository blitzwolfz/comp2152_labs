# person.py

class Person:
    def __init__(self, name, age, height):
        print("Constructing the Person object")
        self.__name = name
        self.__age = age
        self.__height = height
        self.public_prop = "I'm public"

    # Using magic getter and setter for name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __del__(self):
        print("The garbage collector is automatically destroying the Person object")
