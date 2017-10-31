# euler 6 problem
#   Matthew Huber, 3-19-2013


#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#What is the 10 001st prime number?

import math

# correct but poor performance
def getPrime(num):
    primes = [2]
    current = 3

    while len(primes) < num:
        for i in range( len(primes) ):
            if current % primes[i] == 0:
                current += 2
                break
            elif i == len(primes)-1:
                primes.append(current)

    return primes[num-1]


def isPrime(num):
    if num == 2 or num == 3:
        return True
    for i in range(2, int (math.sqrt(num))+1 ):
        if num % i == 0:
            return False
        elif i == int(math.sqrt(num)):
            return True

# this is much faster than getPrime
def getPrime2(num):
    current = 1
    i = 0

    while(i < num):
        current += 1
        if isPrime(current):
            i += 1

    return current

number = int( input() )
#result = getPrime(number)
result = getPrime2(number)

print(result)





