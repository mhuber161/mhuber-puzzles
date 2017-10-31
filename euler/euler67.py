# euler problem 67
#   Matthew Huber, 3-25-2013



# By starting at the top of the triangle below and moving to adjacent 
# numbers on the row below, the maximum total from top to bottom is 23.
# 
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# 
# That is, 3 + 7 + 4 + 9 = 23.
# 
# Find the maximum total from top to bottom in triangle.txt, a 15K 
# text file containing a triangle with one-hundred rows.
# 
# Note: This is a much more difficult version of Problem 18. It is not 
# possible to try every route to solve this problem, as there are 2^99 
# altogether! If you could check one trillion (10^12) routes every second 
# it would take over twenty billion years to check them all. There is an 
# efficient algorithm to solve it. ;o)

import fileinput

# convert string to int matrix, size is length of last row
def setupMatrix(fileName, size):
    matrix = [[]]*size
    # for i in range(size):     #add ith row to matrix
    i=0
    for line in fileinput.input(fileName):  # go through each line
        #print(line)
        offset = 0
        row = []
        for j in range(i+1): 
            offset = 3*j
            row.append( int(line[offset]+line[offset+1]) )
        matrix[i] = row
        i += 1

    return matrix

# print matrix in nice format
def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

# returns value of largest child at specified coordinates
def getMaxChild(matrix,r,c):
    if r == len(matrix)-1:
        return 0

    value1 = matrix[r+1][c]
    value2 = matrix[r+1][c+1]

    if value1 > value2:
        return value1
    else:
        return value2

# from bottom row to top, compute what the max route is at each spot
#   it will just be the largest child for the 2nd to last row
#   we update the matrix to hold the new value and continue
def simplifyMatrix(matrix):
    for i in reversed(range(len(matrix))):    # rows
        for j in range(i+1):
            matrix[i][j] += getMaxChild(matrix,i,j)
        


triMatrix = setupMatrix( "triangle.txt", 100 )
# miniMatrix = setupMatrix( miniTriangleString, 4 )

#printMatrix( triMatrix )
simplifyMatrix( triMatrix )
print ( triMatrix[0][0] ) #holds the max length route

