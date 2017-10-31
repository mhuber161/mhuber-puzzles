

# Starting in the top left corner of a 2×2 grid, and only being able to 
# 	move to the right and down, there are exactly 6 routes to the 
# 	bottom right corner.
# 
# How many such routes are there through a 20×20 grid?

# each box, either go down or right
# max down and right are 20 moves each
# max combo of right and left

# 20r, 20d
# 19r, 20d, 1r

# all options for 20r, 19r, 18r...

# 19r: 20d, 1r or 1d, 1r, 19d or 2d, 1r, 18d

# 0r: 1-20d, 1-20r...

# # find n routes in nxn grid
# def findRoutes(n):
#     routes = 0  # total # 
#     down = 0    # current down moves made
#     right = 0   # current right moves made
#     moveStack = [ (n,n) ]
# 
#     for i in range(0,n+1):  # first right move
#         right = i
#         if i == n: return routes + 1
# 
#         #while j < n and k < n:
# 
#         for j in range(1, n-down+1): # down move
#             down += j
#             print("down")
#             if down == n:
#                 routes += 1
#                 lastMove = moveStack.pop()
#                 down = lastMove[0]
#                 right = lastMove[1]
# 
#             for k in range(1, n-right+1): # right move
#                 right += k
#                 print("right")
#                 if right == n: 
#                     routes += 1
#                     lastMove = moveStack.pop()
#                     down = lastMove[0]
#                     right = lastMove[1]
#                 else:
#                     moveStack.append( (down,right) )
# 
# 
# 
# 
# # find n routes in nxn grid
# def findRoutes2(n):
#     routes = 0  # total # 
#     down = 0    # current down moves made
#     right = 0   # current right moves made
#     for i in range(0,n+1):  # first right move
#         right = i
#         for j in range(1, n+1): # down move
#             # down += j
#             if i == 0: j = n
#             routes += recurseRoutes(n,i,j)
# 
#     return routes
# 
# 
# # returns # of routes from certain point in grid
# def recurseRoutes(n,r,d):
#     routes = 0
#     if r == n or d == n:
#         return 1
#     for i in range(0,n-r+1):
#         for j in range(1,n-d+1):
#             if i == 0: 
#                 j = n
#                 d = 0
#             routes += recurseRoutes(n,r+i,d+j)
#     return routes


# addRoutePoints is quite fast, much better than going through
#   each route separately, only need simple addition

# each point in grid has a route number associated with it
#   to find routes at any point, add up routes at point to the right
#   and below the current point
def addRoutePoints(n):
    points = [ [0 for x in range(n+1)] for y in range(n+1)]
    # borders have only one route
    for i in range(n+1):
        points[i][n] = 1
        points[n][i] = 1
   
    # fills each point going from 2nd to last row and column to first
    for i in reversed(range(n)):
        for j in reversed(range(n)):
            # compute points on jth row and column
            points[j][i] = points[i+1][j] + points[i][j+1]
            points[i][j] = points[i+1][j] + points[i][j+1]

    # return top left point value
    return points[0][0]


result = addRoutePoints(20)

print( result )


