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


# 9.Reverse a number
def reverse_number(number):
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = (reverse * 10) + digit
        number //= 10

    print("Reverse:", reverse)

reverse_number(12345)
print("=================")


# 10.Check armstrong number
def check_armstrong(number):
    original = number
    digits = 0
    temp = number

    while temp > 0:
        digits += 1
        temp //= 10

    total = 0
    temp = number

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == original:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")

check_armstrong(153)
print("=================")


################################################################################################
######                                    Function without input and with return
################################################################################################


# 1.Return Sum
def find_sum():
    a = 10
    b = 20
    return a + b

result = find_sum()
print("Sum:", result)
print("=================")


#2.Return Largest Number
def largest():
    a = 25
    b = 40

    if a > b:
        return a
    else:
        return b

result = largest()
print("Largest:", result)
print("=================")


# 3.Return Factorial
def factorial():
    number = 5
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result

result = factorial()
print("Factorial:", result)
print("=================")


#4. Return Square
def square():
    number = 8
    return number * number

result = square()
print("Square:", result)
print("=================")


#5.Return Sum of 1–20
def find_sum():
    total = 0

    for i in range(1, 21):
        total += i

    return total

result = find_sum()
print("Sum:", result)
print("=================")


#6.Return Digit Count
def count_digits():
    number = 123456
    count = 0

    while number > 0:
        count += 1
        number //= 10

    return count

result = count_digits()
print("Number of digits:", result)
print("=================")


#7.Return Reverse
def reverse_number():
    number = 12345
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = (reverse * 10) + digit
        number //= 10

    return reverse

result = reverse_number()
print("Reverse:", result)
print("=================")


#8.Return Palindrome Result
def palindrome():
    number = 121
    original = number
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = (reverse * 10) + digit
        number //= 10

    if original == reverse:
        return True
    else:
        return False

result = palindrome()

if result:
    print("Palindrome")
else:
    print("Not a palindrome")
print("=================")


#9.Return Prime Result
def prime():
    number = 17
    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False

result = prime()

if result:
    print("Prime number")
else:
    print("Not a prime number")
print("=================")


#10. Return Armstrong Result
def armstrong():
    number = 153
    original = number
    total = 0

    while number > 0:
        digit = number % 10
        total += digit ** 3
        number //= 10

    if total == original:
        return True
    else:
        return False

result = armstrong()

if result:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
print("=================")

################################################################################################
######                                    Function with input and with return 
################################################################################################
 

# ============================================================
# 31. Even or Odd
# Named Function - With Input & With Return
# ============================================================

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


result = check_even_odd(24)
print("31. Result:", result)


# ============================================================
# 32. Positive / Negative / Zero
# ============================================================

def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


result = check_number(-10)
print("32. Result:", result)


# ============================================================
# 33. Largest of Three Numbers
# ============================================================

def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


result = largest(25, 70, 45)
print("33. Largest:", result)


# ============================================================
# 34. Factorial
# ============================================================

def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


result = factorial(5)
print("34. Factorial:", result)


# ============================================================
# 35. Prime Number
# ============================================================

def check_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


result = check_prime(19)

if result:
    print("35. Prime number")
else:
    print("35. Not a prime number")


# ============================================================
# 36. Fibonacci Series
# ============================================================

def fibonacci(number):
    series = []
    a = 0
    b = 1

    for i in range(number):
        series.append(a)
        a, b = b, a + b

    return series


result = fibonacci(10)
print("36. Fibonacci:", result)


# ============================================================
# 37. Reverse a Number
# ============================================================

def reverse_number(number):
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = (reverse * 10) + digit
        number //= 10

    return reverse


result = reverse_number(12345)
print("37. Reverse:", result)


# ============================================================
# 38. Palindrome Number
# ============================================================

def palindrome(number):
    original = number
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = (reverse * 10) + digit
        number //= 10

    return original == reverse


result = palindrome(121)

if result:
    print("38. Palindrome")
else:
    print("38. Not a palindrome")


# ============================================================
# 39. Armstrong Number
# ============================================================

def armstrong(number):
    original = number
    digits = len(str(number))
    total = 0

    while number > 0:
        digit = number % 10
        total += digit ** digits
        number //= 10

    return original == total


result = armstrong(153)

if result:
    print("39. Armstrong number")
else:
    print("39. Not an Armstrong number")


# ============================================================
# 40. Prime Numbers in a Range
# ============================================================

def prime_numbers(start, end):
    primes = []

    for number in range(start, end + 1):

        if number < 2:
            continue

        is_prime = True

        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(number)

    return primes


result = prime_numbers(1, 50)
print("40. Prime numbers:", result)