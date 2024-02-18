#---Basic Programs---
#Basic Program 1
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = num1 + num2

print(f"The sum of {num1} and {num2} is {sum}")



#Basic Program 2
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))

max_value=max(num1,num2)

print(f"The maximum of {num1} and {num2} is: {max_value}")



#Basic Program 3
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
num=int(input("Enter the number to calculate its factorial:"))
if num < 0:
    print("Factorial is not defined for negative number.")
else:
    result=factorial(num)
    print(f"The factorial of {num} is: {result}")



#Basic Program 4
def simple_interest(principal, rate, time):
    interest=(principal*rate*time)/100
    return interest

principal_amount=float(input("Enter the principal amount:"))
interest_rate=float(input("Enter the annual interest(in percentage):"))
time_period=float(input("Enter the time period(in years):"))

result=simple_interest(principal_amount, interest_rate, time_period)
print(f"The simple interest is:{result:.2f}")



#Basic Program 5
def compound_interest(principal,rate,time):
    amount=principal*(1+rate/100)** time
    interest=amount-principal
    return interest
principal_amount=float(input("Enter the principal amount:"))
interest_rate=float(input("Enter the annual interest rate(in percentage):"))
time_period=float(input("Enter the time period(in years):"))

result=compound_interest(principal_amount, interest_rate, time_period)
print(f"The compound interest is:{result:.2f}")



#Basic Program 6
def is_armstrong_number(number):
    num_digits = len(str(number))
    temp = number
    sum_of_cubes = 0

    while temp>0:
        digit = temp%10
        sum_of_cubes += digit**num_digits
        temp //= 10

    return number == sum_of_cubes

num = int(input("Enter a number to check if it's a Armstrong Number:"))
if is_armstrong_number(num):
    print(f"{num} is a Armstrong Number.")
else:
    print(f"{num} is not an Armstrong Number.")



#Basic Program 7
import math

def area_of_circle(radius):
    area = math.pi * radius ** 2
    return area

radius = float(input("Enter the radius of the circle:"))

result = area_of_circle(radius)
print(f"The area of the circle with radius {radius} is: {result:.2f}")



#Basic Program 8
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_in_interval(start, end):
    print(f"Prime numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

start_num = int(input("Enter the start of the interval: "))
end_num = int(input("Enter the end of the interval: "))

print_primes_in_interval(start_num, end_num)



#Basic Program 9
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number to check if it's prime: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")



#Basic Program 10
def nth_fibonacci_number(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

n = int(input("Enter the value of n to find the nth Fibonacci number: "))

result = nth_fibonacci_number(n)
print(f"The {n}th Fibonacci number is: {result}")



#Basic Program 11
def is_perfect_square(num):
    square_root = int(num**0.5)
    return square_root * square_root == num

def is_fibonacci_number(num):
    return is_perfect_square(5 * num**2 + 4) or is_perfect_square(5 * num**2 - 4)

number = int(input("Enter a number to check if it's a Fibonacci number: "))

if is_fibonacci_number(number):
    print(f"{number} is a Fibonacci number.")
else:
    print(f"{number} is not a Fibonacci number.")



#Basic Program 12
def find_nth_multiple_in_fibonacci(n, number):
    fib_sequence = [0, 1]
    
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
        
        if next_fib % number == 0:
            n -= 1
            if n == 0:
                return next_fib

n = int(input("Enter the value of n: "))
number = int(input("Enter the number to find its nth multiple in the Fibonacci series: "))

result = find_nth_multiple_in_fibonacci(n, number)

print(f"The {n}th multiple of {number} in Fibonacci series is: {result}")



#Basic Program 13
char = input("Enter a character: ")

ascii_value = ord(char)

print(f"The ASCII value of '{char}' is: {ascii_value}")



#Basic Program 14
def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6

n = int(input("Enter the value of n: "))

result = sum_of_squares(n)
print(f"The sum of squares of the first {n} natural numbers is: {result}")



#Basic Program 15
def sum_of_cubes(n):
    return (n * (n + 1) // 2)**2

n = int(input("Enter the value of n: "))

result = sum_of_cubes(n)
print(f"The sum of cubes of the first {n} natural numbers is: {result}")
