# euler 5 problem
#   Matthew Huber, 3-19,2013

#2520 is the smallest number that can be divided by each of the numbers from 
#    1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the 
#   numbers from 1 to 20?


# don't need to check 2,3,4,5,6,7,8,9,10 because if the rest of the numbers are
#   divisible, they are too because they are factors of them


def findMaxBruteForce():
    result = 20

    while(True):
        for i in range(11,21):
            if result % i != 0:
                result += 20
                break
        if i == 20:
            return result

print( findMaxBruteForce() )    # brute force method

print(11* 2*2*3 * 13 * 7 * 5 *2*2* 17* 3 * 19)  # prime factorization method



