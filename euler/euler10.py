# euler problem 10
#   Matthew Huber, 3-21-2013

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#Find the sum of all the primes below two million.

import math


# least amount of comparisons to determine if prime
def isPrimeWithList(num,primes):
    for i in range(0, len(primes) ):
        prime = primes[i]
        if prime > int (math.sqrt(num)):
            return True
        elif num % prime == 0:
          return False

# return sum of list of primes under n
def computePrimesSum(n):
    current = 3
    primes = [2]

    while(current < n):
        if isPrimeWithList(current,primes):
            primes.append(current)
        current += 2            # better way to choose next possible prime?

    return sum(primes)



primes = computePrimesSum( 2000000 )

print(primes)
            

