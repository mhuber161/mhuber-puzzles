# euler problem 9
#   Matthew Huber, 3-20-2013

# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
# 
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


#   a < b < c
#   a + b + c = 1000
#   a^2 + b^2 = c^2
#
#   return a*b*c

# a's range is from 1 to 332
# b's range is from 2 to 334

# possibly a faster solution by combining equations above?

def findTrip():
    for i in range(1,333):
        for j in range(1,335):
            a = i
            b = a+j
            c = 1000 - a - b
            if a < b and b < c:
                if a**2 + b**2 == c**2:
                    return a*b*c

result = findTrip()
print ( result )

