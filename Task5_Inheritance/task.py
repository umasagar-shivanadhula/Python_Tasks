# ============================================================
#                SINGLE INHERITANCE
# ============================================================


# ============================================================
# 1. Single Inheritance WITHOUT CONSTRUCTOR
# ============================================================

class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


car = Car()

car.start()      # Inherited method
car.drive()      # Child method

print("----------------------------")


# ============================================================
# 2. Single Inheritance WITH CONSTRUCTOR
# ============================================================

class Person:
    def __init__(self):
        self.name = "Sagar"

    def display_person(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self):
        self.roll_number = 101

    def display_student(self):
        print("Roll Number:", self.roll_number)


student = Student()

# Parent constructor is NOT automatically called
student.display_student()

print("----------------------------")


# ============================================================
# 3. Single Inheritance WITH CONSTRUCTOR + super()
# ============================================================

class Employee:
    def __init__(self, name):
        self.name = name

    def display_employee(self):
        print("Employee Name:", self.name)


class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def display_manager(self):
        print("Employee Name:", self.name)
        print("Department:", self.department)


manager = Manager("Rahul", "IT")

manager.display_manager()

print("----------------------------")


# ============================================================
# 4. Single Inheritance WITH CONSTRUCTOR + super()
# ============================================================

class Animal:
    def __init__(self, name):
        self.name = name

    def display_animal(self):
        print("Animal Name:", self.name)


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def display_dog(self):
        print("Animal Name:", self.name)
        print("Breed:", self.breed)


dog = Dog("Tommy", "German Shepherd")

dog.display_dog()

print("\n============================")
print("       MULTIPLE INHERITANCE")
print("============================")


# ============================================================
# 5. Multiple Inheritance WITHOUT CONSTRUCTOR
# ============================================================

class Camera:
    def take_photo(self):
        print("Camera takes photos")


class MusicPlayer:
    def play_music(self):
        print("Music player plays music")


class Smartphone(Camera, MusicPlayer):
    def make_call(self):
        print("Smartphone makes calls")


phone = Smartphone()

phone.take_photo()
phone.play_music()
phone.make_call()

print("----------------------------")


# ============================================================
# 6. Multiple Inheritance WITH CONSTRUCTOR
# ============================================================

class Father:
    def __init__(self):
        self.father_name = "Ramesh"

    def display_father(self):
        print("Father Name:", self.father_name)


class Mother:
    def __init__(self):
        self.mother_name = "Lakshmi"

    def display_mother(self):
        print("Mother Name:", self.mother_name)


class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        self.child_name = "Rahul"

    def display_child(self):
        print("Child Name:", self.child_name)


child = Child()

child.display_father()
child.display_mother()
child.display_child()

print("----------------------------")


# ============================================================
# 7. Multiple Inheritance WITH CONSTRUCTOR + super()
# ============================================================

class Teacher:
    def __init__(self, teacher_name, **kwargs):
        self.teacher_name = teacher_name
        super().__init__(**kwargs)

    def display_teacher(self):
        print("Teacher Name:", self.teacher_name)


class Researcher:
    def __init__(self, research_area, **kwargs):
        self.research_area = research_area
        super().__init__(**kwargs)

    def display_researcher(self):
        print("Research Area:", self.research_area)


class Professor(Teacher, Researcher):
    def __init__(self, teacher_name, research_area):
        super().__init__(
            teacher_name=teacher_name,
            research_area=research_area
        )

    def display_professor(self):
        print("Professor Details")
        print("Teacher Name:", self.teacher_name)
        print("Research Area:", self.research_area)


professor = Professor("Dr. Arun", "Artificial Intelligence")

professor.display_professor()

print("----------------------------")


# ============================================================
# 8. Multiple Inheritance WITH CONSTRUCTOR + super()
# ============================================================

class Writer:
    def __init__(self, book_name, **kwargs):
        self.book_name = book_name
        super().__init__(**kwargs)

    def display_writer(self):
        print("Book Name:", self.book_name)


class Speaker:
    def __init__(self, language, **kwargs):
        self.language = language
        super().__init__(**kwargs)

    def display_speaker(self):
        print("Language:", self.language)


class Author(Writer, Speaker):
    def __init__(self, book_name, language):
        super().__init__(
            book_name=book_name,
            language=language
        )

    def display_author(self):
        print("Author Details")
        print("Book Name:", self.book_name)
        print("Language:", self.language)


author = Author("Python Programming", "English")

author.display_author()