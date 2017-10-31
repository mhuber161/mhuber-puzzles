# euler problem 3
#   Matthew Huber, 3-18-2013

#'''
#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?
#'''

# primes: 2,3,5,7,11,13,17,19,23,29,31...

import math


testNumber = 13195

number = 600851475143

primes = [2]

#'''
## generate list of primes
## what should the max range be?
#for i in range(2, 10000):
#    for j in range(len(primes)):
#        if i % primes[j] == 0:
#            break
#        else:
#            if j == len(primes)-1:
#                primes.append(i)
#
#print(primes)
#'''

def getPrimeFac(num):
    for i in range(2,int(math.sqrt(num)+1)):   # optimize further?
        if number % i != 0:
            continue
        for j in range(len(primes)):
            if i % primes[j] == 0:
                break
            else:
                if (j == len(primes)-1):
                    primes.append(i)


#getPrimeFac(testNumber)
#getPrimeFac(100000000000)
getPrimeFac(number)

print(primes.pop()) # print last element of primes, the largest prime factor




