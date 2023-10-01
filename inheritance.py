# all classes in Python are a child class of the 'object' class.
class Person:
    def __init__(self,name,age,occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def say_hello(self):
        return f"Hello, my name is {self.name}!"

    def say_age(self):
        return f"I am {self.age} years old!"

class Superhero(Person):
    pass

hero = Superhero("Jessica",29,"Investigative Journalist")
print(hero.say_hello())
print(hero.occupation)
print(hero.say_age())

# using super() keyword

class Person:
    def __init__(self,name,age,occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def say_hello(self):
        return f"Hello, my name is {self.name}!"

    def say_age(self):
        return f"I am {self.age} years old!"

class Superhero(Person):

    def __init__(self,name,age,occupation):
        super().__init__(name,age,occupation)

    def say_two_things(self):
        super().say_hello()
        super().say_age()

hero = Superhero("Wonder Women",27,"Intelligence Officer")
print(hero.say_hello())
print(hero.say_age())
print(hero.occupation)

# print(help(Superhero))
# print(help(Person))


# Inheritance Hierarchy determine using functions
# isinstance()

class ClassA:
    pass

class ClassB(ClassA):
    pass

class ClassC:
    pass

class ClassD(ClassC):
    pass

object_a = ClassA()
object_b = ClassB()
object_c = ClassC()
object_d = ClassD()


print(isinstance(object_b,ClassA))
print(isinstance(object_d,ClassC))
print(isinstance(object_a,ClassA))
print(isinstance(object_b,ClassC))
print(isinstance(object_d,ClassA))
# issubclass

print("issubclass")
print(issubclass(ClassB,ClassA))
print(issubclass(ClassD,ClassC))
print(issubclass(ClassD,ClassA))
print(issubclass(ClassA,ClassB))

# Extending a class

class Person:
    def __init__(self,name,age,occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def say_hello(self):
        return f"Hello, my name is {self.name}!"

    def say_age(self):
        return f"I am {self.age} years old!"

class Superhero(Person):

    def __init__(self,name,age,occupation,secret_identity,nemesis):
        super().__init__(name,age,occupation)
        self.secret_identity = secret_identity
        self.nemesis = nemesis

    def reveal_secret_identity(self):
        return f"My real name is {self.secret_identity}."

    def say_nemesis(self):
        return f"My nemesis is {self.nemesis}."

hero = Superhero("Spider-Man",19,"student","Peter Parker","Doc Octopus")
print(hero.reveal_secret_identity())
print(hero.say_nemesis())

# Method Overriding

class Person:
    def __init__(self,name,age,occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def say_hello(self):
        return f"Hello, my name is {self.name}!"

    def say_age(self):
        return f"I am {self.age} years old!"

class Superhero(Person):

    def __init__(self,name,age,occupation,secret_identity,nemesis):
        super().__init__(name,age,occupation)
        self.secret_identity = secret_identity
        self.nemesis = nemesis

    def reveal_secret_identity(self):
        return f"My real name is {self.secret_identity}."

    def say_nemesis(self):
        return f"My nemesis is {self.nemesis}."

    def say_hello(self):
        return f"Hello myself {self.name},and I am a best comic character."

    def say_age(self):
        return f"I am {self.age} years old,but age is just a number."


hero = Superhero("Ramonda", 40, "Queen of Wakanda", "Ororo Munroe", "Shadow King")
print(hero.say_hello())
print(hero.say_age())

print(help(Superhero))


# Multiple Inheritance

class Dinosaur:
    def __init__(self, size, weight):
        self.size = size
        self.weight = weight
class Carnivore:
    def __init__(self, diet):
        self.diet = diet

class Tyrannosaurus(Dinosaur,Carnivore):
    pass

tiny = Tyrannosaurus(12,14) # it runs the constructor of Dinosaur first
print(tiny.size)

class Tyrannosaurus(Carnivore,Dinosaur):
    pass

tiny = Tyrannosaurus("whatever it wants") # it runs the constructor of Carnivore first
print(tiny.diet)

# Override the init method

class Dinosaur:
    def __init__(self,size,weight):
        self.size = size
        self.weight = weight

class Carnivore:
    def __init__(self,diet):
        self.diet = diet

class Tyrannosaurus(Dinosaur,Carnivore):
    def __init__(self,size,weight,diet):
        Dinosaur.__init__(self,size,weight) # In multiple Inheritance we use self when calling the method from parent class
        Carnivore.__init__(self,diet)  # we can't use super() when overriding the init method.


tiny = Tyrannosaurus(12,14,"whatever it wants")
print(tiny.size)
print(tiny.weight)
print(tiny.diet)

# Another example of multiple inheritance

class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Artist:
  def __init__(self, style):
    self.style = style

class Art_Student(Human, Artist):
  def __init__(self,name,age,style):
      Human.__init__(self,name,age)
      Artist.__init__(self,style)


student = Art_Student("Roberta", 19, "cubism")
print(student.name)
print(student.age)
print(student.style)


# Multiple Inheritance Hierarchy

class A:
  pass

class B:
  pass

class C:
  pass

class D(A,B):
  pass

obj = D()

print(isinstance(obj,D))
print(isinstance(obj,A))
print(isinstance(obj,B))
print(isinstance(obj,C)) # it returns false because obj is not an instance of class C
print(issubclass(D,A))
print(issubclass(D,B))
print(issubclass(D,C)) # it returns false because D is not the subclass of C.


# Method Resolution Order

class A:
    def hello(self):
        print("Hello from class A")


class B:
    def hello(self):
        print("Hello from class B")

class C(A, B):
  def hello(self):
    super().hello()


obj = C()
obj.hello()

print(C.mro())  # method resolution order

# second example

class One:
  def example_method_one(self):
    return "I am from class One"

class Two:
  def example_method_two(self):
    return "I am from class Two"

class Three(Two, One):
  def example_method_three(self):
    return "I am from class Three"

obj = Three()
print(obj.example_method_three())
print(Three.mro())

# Extending a class with multiple Inheritance

class A:
  def hello(self):
    print("Hello from class A")

class B:
  def hello(self):
    print("Hello from class B")

class C(A, B):
  def bonjour(self):
    print("Bonjour!")

  def goodbye(self):
    print("Goodbye.")

obj= C()
obj.bonjour()
obj.goodbye()

# Overriding a Method with Multiple Inheritance

class A:
  def hello(self):
    print("Hello from class A")

class B:
  def hello(self):
    print("Hello from class B")

class C(A, B):
  def hello(self):
    print("Hello from class C")
    super().hello() # because of mro it calls the method of class A
    B.hello(self) # calling hello method from B.

obj= C()
obj.hello()