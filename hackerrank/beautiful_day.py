def getNumberReverse(num):
    reverseNum = 0
    while num >= 10:
        lastNum = num%10
        reverseNum*=10
        reverseNum+=lastNum
        num//=10
    reverseNum*=10
    reverseNum+=num
    print(reverseNum)
    
    

def beautifulDays(i, j, k):
    # Write your code here
    for dayNumber in range(i,j+1):
        getNumberReverse(dayNumber)
beautifulDays(20,23,6)