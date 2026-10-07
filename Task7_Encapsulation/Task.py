
#################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################

# Create a Bank class with the following requirements:
# - Customer name maintain cheyyali.
# - Customer account number maintain cheyyali.
# - Customer balance maintain cheyyali.
# - Name, account number, balance ni private attributes ga maintain cheyyali.
# - Account ki daily withdrawal limit ₹1,00,000 undali.
# - deposit() method create cheyyali.
#   - Deposit chesina amount balance ki add avvali.
#   - Successful deposit ki proper message ravali.
# - withdrawal() method create cheyyali.
#   - Withdrawal amount balance kanna ekkuva unte "Insufficient funds" message ravali.
#   - Withdrawal amount ₹1,00,000 kanna ekkuva unte "Daily withdrawal limit exceeded" message ravali.
#   - Valid withdrawal ayithe balance nunchi amount deduct avvali.
#   - Successful withdrawal ki proper message ravali.
# - get_details() method tho:
#        - Customer name, - Account number, - Current balance display cheyyali.

class Bank:
    def __init__(self, name, acc_no, balance):
        self.__name = name
        self.__acc_no = acc_no
        self.__balance = balance
        self.__daily_limit = 100000

    def deposit(self, money):
        self.__balance += money
        return f"Rs.{money} deposited successfully"

    def withdrawl(self, money):
        if money > self.__daily_limit:
            print("Withdrawl Failed")
            return f"Daily withdrawal limit is Rs.{self.__daily_limit} but ur withdrawl amount is {money}"

        if money <= self.__balance:
            self.__balance -= money
            return f"Rs.{money} withdrawn successfully"
        else:
            return "Insufficient funds"

    def get_details(self):
        return self.__name, self.__acc_no, self.__balance


# Object creation
obj1 = Bank("Sagar", 12345, 140000)

# Display account details
print("Current details:", obj1.get_details())
print()

# Deposit money
print(obj1.deposit(100000))
print("Account details after deposit:", obj1.get_details())
print()

# Withdraw money
print(obj1.withdrawl(1000))
print("Account details after withdrawal:", obj1.get_details())
print()

# Trying to withdraw more than daily limit
print(obj1.withdrawl(150000))
print("Account details:", obj1.get_details())

##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################

# #Create a ShoppingCart system.
# Requirements:
# - Customer name
# - Product name
# - Product price
# - Quantity
# - Add product to cart
# - Increase/decrease quantity
# - Calculate total price
# - Remove product
# - Quantity 0 or negative unte proper message ivvali.
# - Product price and quantity ni private attributes ga maintain cheyyali.

class ShoppingCart:
    def __init__(self,customer_name,product_name,product_price,quantity,add_to_cart):
        self.__customer_name=customer_name
        self.__product_name=product_name
        self.__product_price=product_price
        self.__quantity=quantity
        self.__add_to_cart=add_to_cart
       
    def increase_quantity(self,quantity):
        if quantity>=1:
            self.__quantity+=quantity
            return "quantity increased"
        else:
             return f"{quantity} is less than one"
            
    def decrease_quantity(self,quantity):
        if self.__quantity>=1 and quantity<=self.__quantity and quantity>=1:
            self.__quantity-=quantity
        else:
            return f"{quantity} is less than one" 
    
    def get_details(self):
        self.__total_price=self.__product_price*self.__quantity
        return f"(product: {self.__product_name}, Product Price: {self.__product_price},Quantity: {self.__quantity} ,total price :{self.__total_price})"
    
    def set_cart():
        pass
    
    def get_cart(self):
        if self.__add_to_cart!=True:
            return "no items in cart"
        else:
            print("Card items:")
            return f"(product: {self.__product_name}, Product Price: {self.__product_price},Quantity: {self.__quantity} ,total price :{self.__total_price})"

#invoking
obj1=ShoppingCart("sagar","i phone 16",90000,2,True)
#printing object
print(obj1.get_details())

#increasing quantity
obj1.increase_quantity(2)
print(obj1.get_details())

#decreasing quantity
obj1.increase_quantity(2)
print(obj1.get_details())

#printing cart details
print(obj1.get_cart())
