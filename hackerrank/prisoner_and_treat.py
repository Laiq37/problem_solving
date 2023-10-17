def saveThePrisoner(n, m, s):
    # Write your code here
    # i = m//n
    # if( s-1+m-(n*i) > n):
    #     return s-1+m-(n*i)-n
    # if(s-1== 0 and m-n == 0):
    #     return s-1+m
    # return s-1+m-(n*i)


    # i = 2
    # if(n < m):
    # else:
    #     if(s-1+m > n):
    #         return s-1+m -n
    #     return s-1+m
    # if (n-(m%n))+s-1 > n:
    #    return (n-(m%n))+s-1 - n
    # return (n-(m%n))+s-1

    # m %= n
    # res = (m + s - 1) % n
    # if res == 0:
    #     res = n
    # return res
    m %= n
    lastPrisonerTreat =  (m+s-1)%n
    if lastPrisonerTreat == 0:
        lastPrisonerTreat = n
    return lastPrisonerTreat
print(saveThePrisoner(208526924                ,756265725                 ,150817879))