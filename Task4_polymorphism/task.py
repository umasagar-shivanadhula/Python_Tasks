# ============================================================
# POLYMORPHISM - 10 EXAMPLES
# ============================================================


# ============================================================
# 1. Single Inheritance & Method Overriding
# Online Payment
# ============================================================

class Payment:
    def make_payment(self):
        print("Processing payment")


class UPI(Payment):
    def make_payment(self):
        print("Payment completed through UPI")


payment = UPI()
payment.make_payment()


# ============================================================
# 2. Single Inheritance & Method Overloading
# Food Order
# ============================================================

class FoodOrder:

    def order_food(self, item, quantity=1):
        print("Food:", item)
        print("Quantity:", quantity)


class OnlineFoodOrder(FoodOrder):

    def order_food(self, item, quantity=1):
        print("Online food order")
        print("Food:", item)
        print("Quantity:", quantity)


food_order = OnlineFoodOrder()

food_order.order_food("Pizza")
food_order.order_food("Burger", 2)


# ============================================================
# 3. Multilevel Inheritance & Method Overriding
# Employee Salary
# ============================================================

class Employee:
    def calculate_salary(self):
        print("Calculating employee salary")


class Developer(Employee):
    def calculate_salary(self):
        print("Salary calculated with developer allowance")


class SeniorDeveloper(Developer):
    def calculate_salary(self):
        print("Salary calculated with senior developer allowance")


employee = SeniorDeveloper()
employee.calculate_salary()


# ============================================================
# 4. Multilevel Inheritance & Method Overloading
# E-commerce Product Search
# ============================================================

class ProductSearch:

    def search(self, product, category=None):
        if category is None:
            print("Searching for product:", product)
        else:
            print("Searching for:", product)
            print("Category:", category)


class OnlineStore(ProductSearch):
    pass


class ECommerce(OnlineStore):
    pass


search = ECommerce()

search.search("Laptop")
search.search("Laptop", "Electronics")


# ============================================================
# 5. Hierarchical Inheritance & Method Overriding
# Bank Accounts
# ============================================================

class BankAccount:
    def calculate_interest(self):
        print("Calculating bank interest")


class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Savings account: 4% interest")


class FixedDeposit(BankAccount):
    def calculate_interest(self):
        print("Fixed deposit: 7% interest")


savings = SavingsAccount()
fd = FixedDeposit()

savings.calculate_interest()
fd.calculate_interest()


# ============================================================
# 6. Hierarchical Inheritance & Method Overloading
# Cab Booking
# ============================================================

class CabBooking:

    def book_cab(self, location, cab_type="Mini"):
        print("Pickup Location:", location)
        print("Cab Type:", cab_type)


class Uber(CabBooking):
    pass


class Ola(CabBooking):
    pass


uber = Uber()
ola = Ola()

uber.book_cab("Hyderabad")
uber.book_cab("Hyderabad", "Sedan")

ola.book_cab("Warangal")
ola.book_cab("Warangal", "SUV")


# ============================================================
# 7. Multiple Inheritance & Method Overriding
# Smart Home Device
# ============================================================

class VoiceAssistant:
    def respond(self):
        print("Voice assistant responds")


class SmartLight:
    def respond(self):
        print("Smart light responds to command")


class SmartSpeaker(VoiceAssistant, SmartLight):
    def respond(self):
        print("Smart speaker responds to voice command")


device = SmartSpeaker()
device.respond()


# ============================================================
# 8. Multiple Inheritance & Method Overloading
# Employee Management System
# ============================================================

class EmployeeDetails:

    def display_employee(self, name, department=None):
        if department is None:
            print("Employee Name:", name)
        else:
            print("Employee Name:", name)
            print("Department:", department)


class SalaryDetails:

    def display_employee(self, name, salary=None):
        if salary is None:
            print("Employee:", name)
        else:
            print("Employee:", name)
            print("Salary:", salary)


class EmployeeManagement(EmployeeDetails, SalaryDetails):

    def display_employee(self, name, department=None):
        if department is None:
            print("Employee Name:", name)
        else:
            print("Employee Name:", name)
            print("Department:", department)


management = EmployeeManagement()

management.display_employee("Sagar")
management.display_employee("Sagar", "IT")


# ============================================================
# 9. Hybrid Inheritance & Method Overriding
# Hospital
# ============================================================

class Hospital:
    def treatment(self):
        print("Hospital provides treatment")


class GeneralDepartment(Hospital):
    def treatment(self):
        print("General department provides treatment")


class EmergencyDepartment(Hospital):
    def treatment(self):
        print("Emergency department provides emergency treatment")


class EmergencyDoctor(GeneralDepartment, EmergencyDepartment):
    def treatment(self):
        print("Emergency doctor provides specialized treatment")


doctor = EmergencyDoctor()
doctor.treatment()


# ============================================================
# 10. Hybrid Inheritance & Method Overloading
# Transport System
# ============================================================

class Transport:

    def book(self, vehicle, passengers=1):
        print("Vehicle:", vehicle)
        print("Passengers:", passengers)


class RoadTransport(Transport):
    pass


class WaterTransport(Transport):
    pass


class AmphibiousVehicle(RoadTransport, WaterTransport):
    pass


transport = AmphibiousVehicle()

transport.book("Bus")
transport.book("Boat", 20)