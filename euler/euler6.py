# euler problem 6
#   Matthew Huber, 3-19-2013

#The sum of the squares of the first ten natural numbers is,
#
#1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is,
#
#(1 + 2 + ... + 10)^2 = 55^2 = 3025
#Hence the difference between the sum of the squares of the 
#   first ten natural numbers and the square of the sum is 3025  385 = 2640.
#
#Find the difference between the sum of the squares of the first one 
#   hundred natural numbers and the square of the sum.


# the sqaure of the sum can be simplified to n(n+1)/2
#   (http://en.wikipedia.org/wiki/Summation)

# the sum of the square can be simplified as well: n(n+1)(2n+1)/6


import math

squareOfSums = (100*(100+1)/2)**2

sumOfSquares = 100 * (100+1) * (2*100+1) / 6

result = squareOfSums - sumOfSquares

print(int(result))



