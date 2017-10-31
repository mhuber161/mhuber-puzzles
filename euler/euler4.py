# euler problem 4
#   Matthew Huber, 3-19-2013

#A palindromic number reads the same both ways. The largest palindrome made from 
#   the product of two 2-digit numbers is 9009 = 91  99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.


num1 = 999
num2 = 999

maxPal = 0     # largest palindrome found
palNum1 = 0
palNum2 = 0

mulList = range(0,num2+1)


def isPal(string):
    while len(string) > 0:  
            if string[0] == string[len(string)-1]:  #check first and last char
                string = string[1:len(string)-1]    #check substring
            else:
                break

    if(len(string) < 2):
        return True     
    else:
        return False


# does each multiplication only once, but are they all necessary?
# correct answer happens nearly at end
for i in range(0,num1+1):
    for j in mulList:
        #print(i,"*",j)
        res = i*j
        string = str(res)

        if(isPal(string) and res > maxPal):
            maxPal = res
            palNum1 = i
            palNum2 = j

    mulList = mulList[1:]
            


print(maxPal,": ",palNum1,"*",palNum2)




