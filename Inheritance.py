class Animal:
    def __init__(self,name,lifespan):

        self.name = name
        self.lifespan = lifespan


    def display(self):
        print(f"{self.name},{self.lifespan}")


class Child(Animal):
    def __init__(self,name,lifespan,age):

        self.age = age

        super().__init__(name,lifespan)


    def display(self):

        print("I'm a child1")
        print(f"My age is {self.age}.")


class ChildSecond(Animal):
    def __init__(self,name,lifespan,curr_age):
        self.curr_age = curr_age

        super().__init__(name,lifespan)

    def display(self):

        print("I'm a child 2.")
        print(f"My age is {self.curr_age}.")




c1 = Child("Ragdoll",13, 2)
c2 = ChildSecond("Netherlands Dwarf cat",11, 6)
print(c1.name)

c1.display()
c2.display()

# Inheritance

class GrandFather:

    def __init__(self, name, age, national):
        self.name = name
        self.age = age
        self.national = national

    def __repr__(self):
        return f"{self.name}, {self.age} years old, from {self.national}"

class Father(GrandFather):

    def __init__(self, name, age, national):
        super().__init__(name, age, national)

    def __repr__(self):
        return f"{self.name}, {self.age} years old, from {self.national}"

class Son(Father, GrandFather):

    def __init__(self, name, age, national, education):
        self.education = education
        Father.__init__(self, name, age, national)
        GrandFather.__init__(self, name, age, national)

    def __repr__(self):
        return f"{self.name} has {self.education}"

obj = GrandFather("Williamson", 75, "England")
print(obj.name)
print(repr(obj))

son = Son("John", 30, "USA", "Bachelor's degree")
print(repr(son))