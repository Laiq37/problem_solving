import math


def squares(a, b):
    # Write your code here
    sRange = math.sqrt(a)
    eRange = math.sqrt(b)
    eProperSq = 1
    if (sRange*10) % 10 != 0:
        sRange //=1
        sRange +=1
    if (eRange*10) % 10 != 0:
        eRange //=1
        eRange +=1
        eProperSq = 0
    return int(eRange+(1*eProperSq)  - sRange)
print(squares(24, 49))