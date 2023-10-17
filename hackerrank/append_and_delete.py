def appendAndDelete(s, t, k):
    matchingChar = 0
    for sChar, tChar in zip(s,t):
        if sChar == tChar:
            matchingChar +=1
        else:
            break
    totalNonMatchChar = len(s[matchingChar:])+len(t[matchingChar:])
    if matchingChar == 0 and k >= len(s)+len(t) :
        return 'Yes'
    elif (k >= totalNonMatchChar and ((k%2== 0 and totalNonMatchChar % 2==0) or (k%2== 1 and totalNonMatchChar % 2==1))) or matchingChar == len(t) and totalNonMatchChar+matchingChar < k:
        return 'Yes'
    else:
        return 'No'
    # Write your code here
    # s = [*s]
    # t = [*t]
    # copyT = t
    # if(len(s)> len(t)):
    #     k -= len(s)- len(t)
    #     s = s[0:len(t)]
    # else:
    #     copyT = t[0:len(s)]
    # lastIndex = len(s)
    # isEmpty = False
    # nextItem = 0
    # while k>0:
    #     if len(s) == 0 or lastIndex <= 0:
    #         isEmpty =True
    #         nextItem = len(s)
    #     if isEmpty == False and s == t:
    #         k = 0
    #     elif isEmpty == False and lastIndex >0 and s[lastIndex-1] != copyT[lastIndex-1]:
    #         k-=len(s[lastIndex-1:])
    #         s= s[0: len(s)-(len(s[lastIndex-1:]))]
    #         lastIndex = len(s)
    #     elif isEmpty == False and s[lastIndex-1] == copyT[lastIndex-1]:
    #         lastIndex -=1
    #     elif (len(s)==0 and k > len(t) ) :
    #         k-=1
    #     elif isEmpty and nextItem < len(t):
    #         s.append(t[nextItem])
    #         nextItem =len(s)
    #         k -=1
    #     elif isEmpty and nextItem >= len(t):
    #         k-=1
    #         s.pop()
    # if s == t and k==0:
    #     return 'Yes'
    # return 'No'
print(appendAndDelete('happy','happy',4))