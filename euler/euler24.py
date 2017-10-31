# euler problem 24
#   Matthew Huber, 3-28.2013

# A permutation is an ordered arrangement of objects. For example, 3124 is one 
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations 
# are listed numerically or alphabetically, we call it lexicographic order. The 
# lexicographic permutations of 0, 1 and 2 are:
# 
#     012   021   102   120   201   210
# 
# What is the millionth lexicographic permutation of the digits 
#     0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# there are 10! permutations of the digits
# 10! is 3,628,800
# 9! is 362,880
# 8! is 40320
# 7! is 5040
# 6! is 720
# 5! is 120
# 4! is 24
# 3! is 6
# 2! is 2

# each hundreds palce is 6 permutations
# each thousands place is 24 permutations
# can figure out which number we are at by adding up permutation #s

# 0123456789

#digits = "0123456789"
#digits = ["0","1","2","3","4","5","6","7","8","9"]
digits = [0,1,2,3,4,5,6,7,8,9]

# returns factorial of n
def fac(n):
    result = n
    for i in range(1,n):
        result *= i
    return result

# sort digits after index n in lexicographic order and returns new string
def sortDigits(n):
    #substring = digits[n+1:]
    # insertion sort elements
    for i in range(n+2,len(digits)):
        insertValue = digits[i]
        checkIndex = i
        while checkIndex > n+1 and insertValue < digits[checkIndex-1]:
            digits[ checkIndex ] = digits[ checkIndex -1 ]
            checkIndex -= 1

        digits[ checkIndex ] = insertValue


# return index of next highest number than num in digits[] after start
def getNextHighest(num,start):
    print(start)
    if start == 10:
        return start-2

    for i in [1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]:
        try:
            print(digits[start:],", ",num+i)
            index = digits[start:].index(num+i)
            print(start)
            return index
        except ValueError:
            continue


# returns n lexicographic permutation of 0123456789
def findPerm(n):
    curr = n

    for i in range(0,9):
        while curr > fac(10-i):
            curr -= fac(10-i)
            swapIndex = i+1+getNextHighest(digits[i],i+1)
            print( i,", ",swapIndex,", ",digits[swapIndex] )
            swapVal = digits[i]
            digits[i] = digits[ swapIndex ]
            digits[ swapIndex ] = swapVal
            sortDigits(i)
            #print( curr,",  ",i )
        print("after ",10-i,"! : ",digits)
    print( digits )

findPerm(1000000)
