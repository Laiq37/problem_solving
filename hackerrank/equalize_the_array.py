def equalizeArray(arr):
    elementCounts = {}
    for item in arr:
        if item in elementCounts.keys():
            elementCounts[item] +=1
        else:
            elementCounts[item] = 1
    maxSameValCount = 0
    minExc = 0
    arr = []
    for eleCount in elementCounts.values():
        if maxSameValCount == 0 or maxSameValCount == eleCount:
            minExc += maxSameValCount
            maxSameValCount = eleCount
        elif maxSameValCount > eleCount:
            minExc += eleCount
        else:
            minExc += maxSameValCount
            maxSameValCount = eleCount
    return minExc
print(equalizeArray([2,1,4,4,10,2,4,1,2,4,4]))
# This user is not allowed to logged in new devices