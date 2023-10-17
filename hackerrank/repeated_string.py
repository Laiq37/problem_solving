def repeatedString(s, n):
    aPositions = []
    for i in range(0,len(s)):
        if s[i] == 'a':
            aPositions.append(i)
    fullStringRepeat = n//len(s)
    remaingStringLen = n%len(s)
    repeatedStringCount = fullStringRepeat * len(aPositions)
    for stringPos in aPositions:
        if stringPos < remaingStringLen:
            repeatedStringCount +=1
    return repeatedStringCount
repeatedString('aba',10)