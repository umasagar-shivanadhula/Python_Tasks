# ============================================================
# PYTHON SCOPE WITH CLASSES AND OBJECTS
# ============================================================


# ============================================================
# 1. LOCAL SCOPE INSIDE A METHOD
# ============================================================
# A variable created inside a method is a LOCAL variable.
# It can be accessed only inside that method.

class Student:

    def display(self):

        name = "Sagar"       # Local variable
        age = 22             # Local variable

        print("Name:", name)
        print("Age:", age)


student1 = Student()
student1.display()

# print(name)
# Error: name is local to display()


# ============================================================
# 2. INSTANCE VARIABLES USING __init__()
# ============================================================
# Instance variables belong to individual objects.
# They are created using self inside __init__().
#
# Each object can have different values.

class Student:

    def __init__(self, name, age):

        self.name = name     # Instance variable
        self.age = age       # Instance variable

    def display(self):

        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Sagar", 22)
student2 = Student("Rahul", 23)

student1.display()
student2.display()


# ============================================================
# 3. CLASS VARIABLE
# ============================================================
# A class variable is shared by all objects of the class.
# It is defined directly inside the class.

class Student:

    college = "Malla Reddy University"     # Class variable

    def __init__(self, name):

        self.name = name                    # Instance variable

    def display(self):

        print("Name:", self.name)
        print("College:", Student.college)


student1 = Student("Sagar")
student2 = Student("Rahul")

student1.display()
student2.display()


# ============================================================
# 4. LOCAL + INSTANCE + CLASS VARIABLE
# ============================================================
# This program demonstrates three different scopes:
#
# Local variable    -> inside method
# Instance variable -> self.variable
# Class variable    -> ClassName.variable

class Employee:

    company = "ABC Technologies"       # Class variable

    def __init__(self, name, salary):

        self.name = name                # Instance variable
        self.salary = salary            # Instance variable

    def display(self):

        bonus = 10000                   # Local variable

        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Bonus:", bonus)
        print("Company:", Employee.company)


employee1 = Employee("Sagar", 40000)
employee1.display()


# ============================================================
# 5. GLOBAL VARIABLE + CLASS + OBJECT
# ============================================================
# A global variable is declared outside the class.
# It can be accessed inside class methods.

company_location = "Hyderabad"


class Company:

    def display(self):

        print("Company Location:", company_location)


company1 = Company()
company1.display()


# ============================================================
# 6. GLOBAL + CLASS + INSTANCE + LOCAL
# ============================================================
# Demonstrating different levels of scope together.

country = "India"                       # Global variable


class Student:

    college = "MR University"           # Class variable

    def __init__(self, name):

        self.name = name                # Instance variable

    def display(self):

        course = "AIML"                 # Local variable

        print("Country:", country)
        print("College:", Student.college)
        print("Name:", self.name)
        print("Course:", course)


student1 = Student("Sagar")
student1.display()


# ============================================================
# 7. ACCESSING CLASS VARIABLE USING OBJECT
# ============================================================
# A class variable can usually be accessed using:
#
# ClassName.variable
# object.variable

class Car:

    wheels = 4

    def __init__(self, brand):

        self.brand = brand

    def display(self):

        print("Brand:", self.brand)
        print("Wheels:", Car.wheels)
        print("Wheels using object:", self.wheels)


car1 = Car("BMW")
car1.display()


# ============================================================
# 8. INSTANCE VARIABLE SCOPE
# ============================================================
# Instance variables belong to a particular object.
# Different objects can contain different values.

class Mobile:

    def __init__(self, brand, price):

        self.brand = brand
        self.price = price

    def display(self):

        print("Brand:", self.brand)
        print("Price:", self.price)


mobile1 = Mobile("Samsung", 30000)
mobile2 = Mobile("Apple", 70000)

mobile1.display()
mobile2.display()


# ============================================================
# 9. MODIFYING INSTANCE VARIABLE
# ============================================================
# We can modify an instance variable using the object.

class Person:

    def __init__(self, name):

        self.name = name

    def display(self):

        print("Name:", self.name)


person1 = Person("Sagar")

person1.display()

person1.name = "Rahul"

person1.display()


# ============================================================
# 10. MODIFYING CLASS VARIABLE
# ============================================================
# Class variables are shared by objects unless an object
# creates its own variable with the same name.

class College:

    college_name = "ABC College"

    def display(self):

        print("College:", College.college_name)


college1 = College()
college2 = College()

college1.display()
college2.display()

College.college_name = "XYZ College"

college1.display()
college2.display()


# ============================================================
# 11. VARIABLE SHADOWING IN CLASS
# ============================================================
# A local variable can have the same name as an instance
# variable or class variable.
#
# Python chooses the most specific scope.

class Employee:

    company = "ABC"

    def __init__(self, name):

        self.name = name

    def display(self):

        name = "Local Name"

        print("Local:", name)
        print("Instance:", self.name)
        print("Class:", Employee.company)


employee1 = Employee("Sagar")
employee1.display()


# ============================================================
# 12. self KEYWORD AND SCOPE
# ============================================================
# self refers to the current object.
#
# self.name means the variable belongs to the object.

class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def display(self):

        print("Object:", self)
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Sagar", 22)
student1.display()


# ============================================================
# 13. LOCAL VARIABLE vs INSTANCE VARIABLE
# ============================================================
# Local variable:
#     Exists only inside the method.
#
# Instance variable:
#     Belongs to the object and can be accessed
#     through self.

class Product:

    def __init__(self, name):

        self.name = name

    def display(self):

        price = 500       # Local variable

        print("Product:", self.name)
        print("Price:", price)


product1 = Product("Laptop")
product1.display()


# ============================================================
# 14. CLASS METHOD AND CLASS VARIABLE
# ============================================================
# @classmethod receives cls instead of self.
# cls refers to the class itself.

class Employee:

    company = "ABC Technologies"

    @classmethod
    def display_company(cls):

        print("Company:", cls.company)


Employee.display_company()


# ============================================================
# 15. STATIC METHOD AND LOCAL SCOPE
# ============================================================
# A static method does not receive self or cls automatically.
# Variables created inside it are local variables.

class Calculator:

    @staticmethod
    def add():

        a = 10
        b = 20

        print("Sum:", a + b)


Calculator.add()


# ============================================================
# 16. NESTED FUNCTION INSIDE CLASS METHOD
# ============================================================
# A method can contain another function.
# The inner function can access variables from the
# enclosing method.

class Company:

    def employee_details(self):

        employee_name = "Sagar"

        def display():

            print("Employee:", employee_name)

        display()


company1 = Company()
company1.employee_details()


# ============================================================
# 17. nonlocal WITH CLASS METHOD
# ============================================================
# nonlocal works with nested functions.
# It modifies a variable from the enclosing function.

class Counter:

    def start(self):

        count = 0

        def increment():

            nonlocal count
            count += 1

            print("Count:", count)

        increment()
        increment()
        increment()


counter1 = Counter()
counter1.start()


# ============================================================
# 18. global KEYWORD INSIDE CLASS METHOD
# ============================================================
# global refers to a variable declared outside the class
# and outside the method.

count = 0


class Counter:

    def increment(self):

        global count

        count += 1

        print("Count:", count)


counter1 = Counter()

counter1.increment()
counter1.increment()
counter1.increment()


# ============================================================
# 19. INHERITANCE AND SCOPE
# ============================================================
# Child class can access variables and methods of parent class.

class Parent:

    parent_name = "Parent Class"

    def display_parent(self):

        print("Parent:", self.parent_name)


class Child(Parent):

    child_name = "Child Class"

    def display_child(self):

        print("Child:", self.child_name)


child1 = Child()

child1.display_parent()
child1.display_child()


# ============================================================
# 20. INSTANCE VARIABLE IN INHERITANCE
# ============================================================
# Child class inherits instance variables from parent class.

class Person:

    def __init__(self, name):

        self.name = name


class Student(Person):

    def display(self):

        print("Student Name:", self.name)


student1 = Student("Sagar")
student1.display()


# ============================================================
# 21. super() AND SCOPE
# ============================================================
# super() is used to access parent class members.

class Person:

    def __init__(self, name):

        self.name = name

    def display(self):

        print("Name:", self.name)


class Student(Person):

    def __init__(self, name, course):

        super().__init__(name)

        self.course = course

    def display(self):

        super().display()

        print("Course:", self.course)


student1 = Student("Sagar", "AIML")
student1.display()


# ============================================================
# 22. LEGB RULE WITH CLASS
# ============================================================
# Important:
#
# L -> Local
# E -> Enclosing
# G -> Global
# B -> Built-in
#
# Class scope is NOT part of the LEGB lookup rule for
# a function defined inside a class.
#
# Instance variables are accessed using self.
# Class variables are accessed using ClassName or cls.

x = "Global"


class Demo:

    x = "Class Variable"

    def display(self):

        x = "Local"

        print("Local:", x)
        print("Class:", Demo.x)
        print("Global:", globals()["x"])


demo1 = Demo()
demo1.display()


# ============================================================
# 23. CLASS SCOPE
# ============================================================
# Variables defined directly inside a class belong to
# the class namespace.

class Student:

    name = "Sagar"
    age = 22

    def display(self):

        print("Name:", Student.name)
        print("Age:", Student.age)


print("Class Name:", Student.name)
print("Class Age:", Student.age)

student1 = Student()
student1.display()


# ============================================================
# 24. __dict__ TO SEE OBJECT SCOPE
# ============================================================
# __dict__ shows the attributes stored inside an object.

class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age


student1 = Student("Sagar", 22)

print("Object Dictionary:")
print(student1.__dict__)


# ============================================================
# 25. __dict__ TO SEE CLASS SCOPE
# ============================================================
# Class.__dict__ shows attributes stored in the class namespace.

class Student:

    college = "MR University"

    def display(self):

        print("Hello")


print("Class Dictionary:")
print(Student.__dict__)


# ============================================================
# 26. COMPLETE SCOPE EXAMPLE
# ============================================================
# This example combines:
#
# Global variable
# Class variable
# Instance variable
# Local variable
# Enclosing variable
# Built-in function
#
# ============================================================

global_name = "Global Sagar"


class Student:

    college = "Malla Reddy University"

    def __init__(self, name):

        self.name = name

    def display(self):

        course = "AIML"

        def inner():

            message = "Welcome"

            print(message)                 # Local
            print(course)                  # Enclosing
            print(self.name)               # Instance
            print(Student.college)         # Class
            print(global_name)             # Global
            print(len(self.name))          # Built-in

        inner()


student1 = Student("Sagar")
student1.display()


# ============================================================
# FINAL SCOPE SUMMARY
# ============================================================
#
# 1. Local Scope
#       Variable inside a function/method.
#
# 2. Enclosing Scope
#       Variable inside an outer function when
#       nested functions are used.
#
# 3. Global Scope
#       Variable declared outside functions/classes.
#
# 4. Built-in Scope
#       Python's predefined names such as:
#       print(), len(), type(), max(), min(), sum()
#
# 5. Class Scope
#       Variables defined directly inside a class.
#
# 6. Instance Scope
#       Variables created using self.variable.
#
# 7. global keyword
#       Used to modify a global variable.
#
# 8. nonlocal keyword
#       Used to modify an enclosing variable.
#
# 9. self
#       Refers to the current object.
#
# 10. cls
#       Refers to the current class in a classmethod.
#
# 11. LEGB
#       Local -> Enclosing -> Global -> Built-in
#
# 12. Important Python Rule
#       if, for and while DO NOT create a new scope.
#       Functions DO create a new scope.
#
# ============================================================

print("\nAll Scope Programs Completed Successfully!")