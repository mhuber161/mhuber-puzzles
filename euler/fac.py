

#def fac(n):return reduce(lambda x,y:x*y,[1]+range(1,n+1))

def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)


facNum = int(input())
res = fac(facNum)

print( "factorial of "+str(facNum)+" is:"+str(res))

