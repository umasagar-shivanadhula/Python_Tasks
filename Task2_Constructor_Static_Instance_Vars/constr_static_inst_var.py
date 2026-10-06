# ============================================================
# Example 1: Bank
# ============================================================

class Bank:

    # Static / Class Variables
    bank_name = "State Bank"
    branch_count = 10

    # Constructor
    def __init__(self, account_holder, account_number, balance, account_type):
        # Instance Variables
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def display(self):
        print("Bank Name:", Bank.bank_name)
        print("Branch Count:", Bank.branch_count)
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        print("Account Type:", self.account_type)
        print("--------------------------")


# Multiple Objects
account1 = Bank("Sagar", 1001, 25000, "Savings")
account2 = Bank("Rahul", 1002, 40000, "Current")
account3 = Bank("Kiran", 1003, 30000, "Savings")

account1.display()
account2.display()
account3.display()


# ============================================================
# Example 2: Student
# ============================================================

class Student:

    # Static / Class Variables
    college_name = "Malla Reddy University"
    college_code = "MRU101"

    # Constructor
    def __init__(self, name, roll_number, age, course):
        # Instance Variables
        self.name = name
        self.roll_number = roll_number
        self.age = age
        self.course = course

    def display(self):
        print("College Name:", Student.college_name)
        print("College Code:", Student.college_code)
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Age:", self.age)
        print("Course:", self.course)
        print("--------------------------")


# Multiple Objects
student1 = Student("Sagar", 101, 22, "CSE")
student2 = Student("Ravi", 102, 21, "AIML")
student3 = Student("Kiran", 103, 22, "ECE")

student1.display()
student2.display()
student3.display()


# ============================================================
# Example 3: Employee
# ============================================================

class Employee:

    # Static / Class Variables
    company_name = "Tech Solutions"
    company_location = "Hyderabad"

    # Constructor
    def __init__(self, name, employee_id, salary, department):
        # Instance Variables
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.department = department

    def display(self):
        print("Company Name:", Employee.company_name)
        print("Company Location:", Employee.company_location)
        print("Employee Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)
        print("Department:", self.department)
        print("--------------------------")


# Multiple Objects
employee1 = Employee("Arjun", 501, 35000, "IT")
employee2 = Employee("Priya", 502, 40000, "HR")
employee3 = Employee("Vijay", 503, 45000, "Finance")

employee1.display()
employee2.display()
employee3.display()