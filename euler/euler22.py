# euler problem 22
#   Matthew Huber, 3-25-2013

# Using names.txt, a 46K text file containing over five-thousand first 
# names, begin by sorting it into alphabetical order. Then working out 
# the alphabetical value for each name, multiply this value by its 
# alphabetical position in the list to obtain a name score.
# 
# For example, when the list is sorted into alphabetical order, COLIN, 
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# So, COLIN would obtain a score of 938 × 53 = 49714.
# 
# What is the total of all the name scores in the file?

# puts names in list
def setupList(fileName):
    f = open(fileName)
    line = f.readline() # all the names on one line
    
    names = []
    nextComma = 0
    prevComma = 0
    while nextComma >= 0:
        prevComma = nextComma
        nextComma = line.find(",",nextComma+1)
        name = line[prevComma+1:nextComma]
        name = name.strip("\"")
        names.append(name)
    
    return names

# return alphabetical value of string n
def getAlphaValue(name):
    value = 0
    for i in range(len(name)):
        value += ord(name[i])-64    #A has ordinal val 65

    return value

# totals all the name scores in list names
def getTotalScore(names):
    totalScore = 0
    for i in range(len(names)):
        totalScore += getAlphaValue(names[i])*(i+1)

    return totalScore
        

namesList = setupList("names.txt")

namesList.sort()

print( getTotalScore(namesList) )
