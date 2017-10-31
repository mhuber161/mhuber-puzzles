# euler problem 18
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
# Find the maximum total from top to bottom of the triangle below:
# 
#     75
#     95 64
#     17 47 82
#     18 35 87 10
#     20 04 82 47 65
#     19 01 23 75 03 34
#     88 02 77 73 07 63 67
#     99 65 04 28 06 16 70 92
#     41 41 26 56 83 40 80 70 33
#     41 48 72 33 47 32 37 16 94 29
#     53 71 44 65 25 43 91 52 97 51 14
#     70 11 33 28 77 73 17 78 39 68 17 57
#     91 71 52 38 17 14 91 43 58 50 27 29 48
#     63 66 04 68 89 53 67 30 73 16 69 87 40 31
#     04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
# 
# Note: As there are only 16384 routes, it is possible to solve this 
# problem by trying every route. However, Problem 67, is the same 
# challenge with a triangle containing one-hundred rows; it cannot be 
# solved by brute force, and requires a clever method! ;o)


miniTriangleString = """03
07 04
02 04 06
08 05 09 03"""

triangleString = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

# convert string to int matrix, size is length of last row
def setupMatrix(triString, size):
    matrix = [[]]*size
    offset = 0
    for i in range(size):     #add ith row to matrix
        row = []
        if i != 0: offset += 3

        for j in range(i+1): 
            if j != 0: offset += 3
            row.append( int(triString[offset]+triString[offset+1]) )

        matrix[i] = row

    return matrix

# #calculate sum of sub-tringle at row r and column c (0 start)
# def calcTriSum(r,c,matrix):    
#     subTotal = matrix[r][c]
#     for i in range(r+1,len(matrix)):    # ith row
#         for j in range(0,i-r+1):          # step through row
#             subTotal += matrix[i][c+j]
# 
#     return subTotal
# 
# # calc sum of going left or going right
# def calcTriSum2(r,c,isLeft,matrix):
#     subTotal = matrix[r][c]
#     for i in range(r+1,len(matrix)):
#         if isLeft:
#             subTotal += matrix[i][c]
#         else:
#             subTotal += matrix[i][c+i-r]
# 
#     return subTotal
# 
# def getMaxRoute(matrix):
#     maxRoute = matrix[0][0]
#     nextBestIndex = 0
#     for i in range(1,len(matrix)):  #ith row
#         nextBestSum = 0
#         index = nextBestIndex        
# 
#         # determine which index to use next
#         for j in range(index,index+2):  #column
#             if i == len(matrix)-1:
#                 subTotal = matrix[i][j]
#             else:
#                 #subTotal = calcTriSum2(i, j,j==index, matrix)
#                 subTotal = calcTriSum(i, j, matrix)
#             if subTotal > nextBestSum:
#                 nextBestIndex = j
#                 nextBestSum = subTotal
#         maxRoute += matrix[i][nextBestIndex]
#     
#     return maxRoute

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
        


triMatrix = setupMatrix( triangleString, 15 )
# miniMatrix = setupMatrix( miniTriangleString, 4 )

simplifyMatrix( triMatrix )
print ( triMatrix[0][0] ) #holds the max length route

