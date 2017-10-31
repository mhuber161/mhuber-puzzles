# euler problem 16
#   Matthew Huber 3-25-2013



# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# 
# What is the sum of the digits of the number 2^1000?

def find2sSum(n):
    string = str(2 << n-1)
    result = 0
    for i in range(len(string)):
        result += int(string[i])

    return result

print(find2sSum(1000))


