################################################################################################
######                                    Function without input and without return 
################################################################################################
 # 1.Print even numbers 1–20
def even_numbers():
    for i in range(1,21):
        if i%2==0:
            print(i)
   
even_numbers()
print("=================")



# 2.Print odd numbers 1–20
def odd_numbers():
    for i in range(1,21):
        if i %2!=0:
            print(i)
odd_numbers()
print("=================")

# 3.Check whether a number is positive/negative
def test_number():
    a=10
    if a%2==0:
        print("Even")
    else:
        print("Odd")
test_number()
print("=================")

# 4.Find sum of 1–N
def sum_of_integers():
    n=10
    sum=0
    for i in range(1,n+1):
        sum+=i
    print(f"sum of 1 to {n}: {sum}")
sum_of_integers()
print("=================")

# 5.Find factorial
def factorial():
    a=5
    factorial=1
    for i in range(1,a+1):
        factorial*=i
    print(f"factorial of {a} is : {factorial}")
factorial()
print("=================")

# 6.Print multiplication table
def multiplication_table():
    a=5
    for i in range(1,11):
        print(f"{a} * {i} = {a*i} ")
multiplication_table()
print("=================")

# 7.Check prime number
def is_prime():
    a=10
    factors=0
    for i in range(2,a):
        if a%i==0:
            factors+=1
    if a<=1:
        print("a is <= 1")
    elif factors==0 :
        print(f"{a} is Prime")
    else:
        print(f"{a} is not Prime")
is_prime()
print("=================")

# 8.Print primes in a range
def primes():
    a=10
    
    for i in range(2,a+1):
        factors=0
        for j in range(2,i):
            if i%j==0:
                factors+=1
        if a<=1:
            print("a is <= 1")
        elif factors==0 :
            print(f"{i} is Prime")
        else:
            print(f"{i} is not Prime")
primes()
print("=================")

# 9.Reverse a number

def reverse_a_number():
    number = 12345
    reverse_number = 0

    while number > 0:
        digit = number % 10
        reverse_number = (reverse_number * 10) + digit
        number //= 10

    print("Reversed number:", reverse_number)

reverse_a_number()
print("=================")

# 10.Check Armstrong number
def is_armstrong():
    z=153
    a=z
    b=len(str(a))
    c=0
    for i in range(b):
        digit=a%10
        c+=digit**b
        a//=10
    if(z==c):
        print("Armstrong")
    else:
        print("Not a Armstrong")
is_armstrong() 
print("=================")

################################################################################################
######                                    Function with input and without return
################################################################################################


# 1.Check even/odd
def check_even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_even_odd(25)
print("=================")


# 2.Check positive/negative/zero
def check_number(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

check_number(-15)


# 3.Find largest of two numbers
def largest(a, b):
    if a > b:
        print("Largest:", a)
    else:
        print("Largest:", b)

largest(25, 40)
print("=================")


# 4.Find largest of three numbers
def largest(a, b, c):
    if a >= b and a >= c:
        print("Largest:", a)
    elif b >= a and b >= c:
        print("Largest:", b)
    else:
        print("Largest:", c)

largest(25, 60, 40)
print("=================")


# 5.Print multiplication table
def multiplication_table(number):
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

multiplication_table(7)
print("=================")


# 6.Find factorial
def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result *= i

    print("Factorial:", result)

factorial(6)
print("=================")


# 7.Check prime
def check_prime(number):
    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        print("Prime number")
    else:
        print("Not a prime number")

check_prime(29)
print("=================")


# 8.Print Fibonacci series
def fibonacci(number):
    a = 0
    b = 1

    for i in range(number):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

fibonacci(10)
print("=================")

print("=================")

print("=================")

print("=================")

print("=================")

print("=================")

print("=================")

print("=================")

print("=================")

print("=================")

print("=================")

print("=================")

print("=================")


