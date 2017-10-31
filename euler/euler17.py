# euler problem 16
#   Matthew Huber, 3-25-2013



# If the numbers 1 to 5 are written out in words: one, two, three, four,
#     five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# 
# If all the numbers from 1 to 1000 (one thousand) inclusive were written 
#     out in words, how many letters would be used?
# 
# Note: Do not count spaces or hyphens. For example, 342 (three hundred 
#     and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
#     contains 20 letters. The use of "and" when writing out numbers is in 
#     compliance with British usage.

counts = {"0":4, "1":3, "2":3, "3":5, "4":4, "5":4, "6":3, "7":5, 
          "8":5, "9":4,"10":3, "11":6, "12":6, "13":8, "14":8,
          "15":7, "16":7, "17":9, "18":8, "19":8, "20":6, "30":6,
          "40":5, "50":5, "60":5, "70":7, "80":6, "90":6}

# gets number letter count of number n (max 1000)
def getLetterCount(n):
    word = str(n)
    count = 0

    if len(word) > 3:   #thousands place
        count += 11
    elif len(word) > 2:   #hundreds place
        count += 7 #hundred = 7
        count += counts[ word[-3] ]
        if int(word[-2:]) > 0:
            count += 3  #and = 3
        
    if len(word) > 1 and int(word[-2:]) > 0:   #tens place
        if int(word[-2:]) > 19: 
            count += counts[ word[-2]+"0" ]
            if int(word[-2:]) % 10 != 0:
                count += counts[ word[-1] ]
        elif int(word[-2:]) > 9:
            count += counts[ word[-2:] ]
        else:
            count += counts[ word[-1] ]
    elif len(word) == 1:
        count += counts[ word[0] ]

    return count

# sum letter counts from 1 to n
def sumLetterCount(n):
    total = 0
    for i in range(1,n+1):
        total += getLetterCount(i) 

    return total

print( sumLetterCount(1000) )
            

# print( "342: ",getLetterCount(342) )
# print( "115: ",getLetterCount(115) )
# print( "1: ",getLetterCount(1) )
# print( "100: ",getLetterCount(100) )
# print( "101: ",getLetterCount(101) )
# print( "292: ",getLetterCount(292) )
# print( "0: ",getLetterCount(0) )
# print( "8: ",getLetterCount(8) )

