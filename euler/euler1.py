# euler problem #1
# Matthew Huber, 3-18-2013

# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
#   we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


upper = 999
total = 0

for i in range(0,upper//3+1): # range(0,334) gives 0 to 333
    total = total + i*3     

#print(total)

for i in range(0,upper//5+1): # 0 to 199
    total = total + i*5

#print(total)

for i in range(0,upper//15+1):  # 0 to 66, removes duplicates
    total = total - i*15

print(total)


