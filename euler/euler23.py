# euler problem 23
#   Matthew Huber, 3-26-2013

# Non-abundant sums
# Problem 23
# 
# A perfect number is a number for which the sum of its proper divisors is 
# exactly equal to the number. For example, the sum of the proper divisors of 
# 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# 
# A number n is called deficient if the sum of its proper divisors is less than 
# n and it is called abundant if this sum exceeds n.
# 
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
# number that can be written as the sum of two abundant numbers is 24. By 
# mathematical analysis, it can be shown that all integers greater than 28123 
# can be written as the sum of two abundant numbers. However, this upper limit 
# cannot be reduced any further by analysis even though it is known that the 
# greatest number that cannot be expressed as the sum of two abundant numbers 
# is less than this limit.
# 
# Find the sum of all the positive integers which cannot be written as the sum 
# of two abundant numbers.


# strategy: find abundant numbers, go through each number and check if it is 
#   the sum of any two abundant numbers

# max abundant number we need to find is less than 28123

import math

# get the sum of the proper divisors of n
def getDivSum(n):
    divSum = 0
    for i in range(1,int(math.sqrt(n)+1) ):
        if n % i == 0:
            divSum += i
            if i != 1 and i < math.sqrt(n):
                divSum += int(n/i)

    return divSum

# return list of abundant numbers under n
def findAbundants(n):
    abundants = []
    for i in range(n):
        if getDivSum(i) > i:
            abundants.append(i)
    
    return abundants

# def isAbunSum(l,checkNum):
#     for i in range(len(l)):
#         if l[i] >= checkNum:
#             return False
#         for j in range(len(l)):
#             if l[j] >= checkNum:
#                 break
#             elif l[i] + l[j] == checkNum:
#                 return True
#     return False
# 
#     
# 
# # check to see what numbers aren't the sum of 2 abundants from list l
# def checkSums(l,n):
#     sumTotal = 0
#     for i in range(1,n):
#         if isAbunSum(l,i) == False:
#             sumTotal += i
#         if i%100 == 0:
#             print (sumTotal)
#     return sumTotal


# returns sum of all numbers that aren't the sum of 2 abundant numbers
def checkSums2(l,n):
    sumList = [False for i in range(n)]
    sumTotal = 0

    for i in range(len(l)):
        for j in range(i,len(l)):
            if l[i]+l[j] < n:
                sumList[ l[i]+l[j] ] = True     #true if index is sum

    for i in range(len(sumList)):
        if sumList[i] == False:     #sum indices that weren't abundant sums
            print(i)
            sumTotal += i

    return sumTotal
        

abunList = findAbundants(28200)

print( checkSums2(abunList, 28200) )

#print( checkSums(abunList,28123) )



