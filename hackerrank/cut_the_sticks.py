def removeShortSticks(minStick, arr):
    i = 0
    while True:
        if len(arr) == 0:
            return arr
        elif arr[i]-minStick == 0:
            arr.pop(i)
            continue
        elif arr[i]-minStick != 0:
            return arr
        i+=1

def cutTheSticks(arr):
    # Write your code here
    arr.sort()
    sticksAfterShortening = [len(arr)]
    while True:
        minStick = arr[0]
        currentArr = arr
        arr = removeShortSticks(minStick,arr)
        if(len(arr) == 0):
            break
        sticksAfterShortening.append(len(arr))
    return sticksAfterShortening


print(cutTheSticks([8, 8, 14, 10, 3, 5, 14, 12]))