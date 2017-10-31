# euler problem 14
#   Matthew Huber, 3-21-2013

# The following iterative sequence is defined for the set of positive integers:
# 
#     n  n/2 (n is even)
#     n  3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
#         13  40  20  10  5  16  8  4  2  1
# 
# It can be seen that this sequence (starting at 13 and finishing at 1) 
# contains 10 terms. Although it has not been proved yet (Collatz Problem), 
# it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# Note: Once the chain starts the terms are allowed to go above one million.


# power of 2: 2^n is length n+1
# hold results of chain length in dict, don't waste computations


# return starting number with longest chain
def computeLongestChain(n):
    longestI = 0
    longestChain = 0
    chains = {1:1}
    for i in range(2,n):
        term = i
        iLength = 0
        getLength = chains.get(term,-1)
        while getLength < 0:
            if term % 2 == 0:
                term = term/2
            else:
                term = 3*term + 1
            getLength = chains.get(term,-1)
            iLength += 1
        iLength += getLength
        chains[i] = iLength

        if iLength > longestChain:
            longestI = i
            longestChain = iLength

    return longestI


result = computeLongestChain(1000000)
print(result)

        

            
        


