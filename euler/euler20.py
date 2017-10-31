# euler problem 20
#   Matthew Huber, 3-25-2013



# n! means n × (n − 1) × ... × 3 × 2 × 1
# 
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# 
# Find the sum of the digits in the number 100!


def factorial(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

def sumNumberString(n):
    nString = str(n)
    total = 0
    for i in range(len(nString)):
        total += int(nString[i])
    return total

number = factorial(100)

print( sumNumberString(number) )

