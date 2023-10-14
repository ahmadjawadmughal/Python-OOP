class Person:

    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def __repr__(self):
        return f"{self.name}, {self.age} years old, from {self.nationality}"

class Wife(Person):

    def __init__(self, name, age, nationality):
        super().__init__(name, age, nationality)

class Son(Person):

    def __init__(self, name, age, nationality):
        super().__init__(name, age, nationality)

obj = Person("Henry", 50, "USA")
obj1 = Wife("Kate", 40, "USA")
obj2 = Son("Kane Henry", 17, "USA")

print(repr(obj))  # Print the __repr__ of obj
print(repr(obj1))  # Print the __repr__ of obj1
print(repr(obj2))  # Print the __repr__ of obj2