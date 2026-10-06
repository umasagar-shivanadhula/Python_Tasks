# ============================================================
# NESTED LOOPS - 10 PROGRAMS
# ============================================================


# 1. Sum of Prime Numbers
# Find the sum of all prime numbers between 20 and 150

total = 0

for num in range(20, 151):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        total += num

print("1. Sum of Prime Numbers:", total)


# ============================================================
# 2. Average of Perfect Numbers
# Find the average of all perfect numbers between 1 and 1000

total = 0
perfect_count = 0

for num in range(1, 1001):
    divisor_sum = 0

    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i

    if divisor_sum == num:
        total += num
        perfect_count += 1

average = total / perfect_count

print("2. Average of Perfect Numbers:", average)


# ============================================================
# 3. Leap Years in a Range
# Print all leap years between 1900 and 2026

print("3. Leap Years:")

for year in range(1900, 2027):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(year, end=" ")

print()


# ============================================================
# 4. Palindrome Numbers
# Print all palindrome numbers between 100 and 500

print("4. Palindrome Numbers:")

for num in range(100, 501):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        print(original, end=" ")

print()


# ============================================================
# 5. Digit Sum = 10
# Print numbers between 120 and 850 whose digit sum is exactly 10

print("5. Numbers with Digit Sum 10:")

for num in range(120, 851):
    temp = num
    digit_sum = 0

    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        temp = temp // 10

    if digit_sum == 10:
        print(num, end=" ")

print()


# ============================================================
# 6. Pairs with Target Sum
# Print pairs (a, b) between 1 and 50 whose sum is 30
# Print each pair only once

print("6. Pairs with Sum 30:")

for a in range(1, 51):
    for b in range(a, 51):
        if a + b == 30:
            print("(", a, ",", b, ")")


# ============================================================
# 7. Exactly 3 Factors
# Print numbers between 10 and 300 having exactly 3 factors

print("7. Numbers with Exactly 3 Factors:")

for num in range(10, 301):
    factor_count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            factor_count += 1

    if factor_count == 3:
        print(num, end=" ")

print()


# ============================================================
# 8. Prime Factors
# Print prime factors of every number between 20 and 50

print("8. Prime Factors:")

for num in range(20, 51):
    print("Prime factors of", num, ":", end=" ")

    for i in range(2, num + 1):

        is_prime = True

        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break

        if is_prime and num % i == 0:
            print(i, end=" ")

    print()


# ============================================================
# 9. Armstrong Numbers
# Print all Armstrong numbers between 100 and 999

print("9. Armstrong Numbers:")

for num in range(100, 1000):
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp = temp // 10

    if total == num:
        print(num, end=" ")

print()


# ============================================================
# 10. Maximum Factors
# Find the number between 50 and 150
# that has the maximum number of factors

max_factors = 0
max_number = 0

for num in range(50, 151):
    factor_count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            factor_count += 1

    if factor_count > max_factors:
        max_factors = factor_count
        max_number = num

print("10. Number with Maximum Factors:", max_number)
print("Number of Factors:", max_factors)