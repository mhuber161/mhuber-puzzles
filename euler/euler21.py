# euler problem 21
#   Matthew Huber, 3-25-2013



# Let d(n) be defined as the sum of proper divisors of n (numbers 
# less than n which divide evenly into n).
# 
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable 
# pair and each of a and b are called amicable numbers.
# 
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 
# 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 
# are 1, 2, 4, 71 and 142; so d(284) = 220.
# 
# Evaluate the sum of all the amicable numbers under 10000.

import math

# return sum of proper divisors of n
def sumDivisors(n):
    sumTotal = 0
    for i in range(1, int(math.sqrt(n)+1)):
        if n % i == 0:
            sumTotal += i
            if i != 1 and i < math.sqrt(n):
                sumTotal += n/i
    return int(sumTotal)

# return sum of all amicable pairs under n
#   can be optimized by eliminating duplicate and 
#   unnecessary runs of sumDivisors
def sumAmiPairs(n):
    total = 0
    for i in range(1,n):
        nCurr = sumDivisors(i)
        amiPair = sumDivisors(nCurr)
        #print("sumD: ",nCurr,", ",amiPair)
        if amiPair == i and nCurr != i:
            #print(nCurr,", ",i)
            total += i
    return total


print (sumAmiPairs(10000))

# print(sumDivisors(220))
# print(sumDivisors(284))
# print(sumDivisors(1))
# print(sumDivisors(2))
# print(sumDivisors(3))
# print(sumDivisors(6))
# print(sumDivisors(18))
# print(sumDivisors(36))

