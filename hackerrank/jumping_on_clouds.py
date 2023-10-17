def jumpingOnClouds(c, k):
    currentIndex = 0
    maxEnergy = 100
    while True:
        currentIndex = (currentIndex+k)%n
        maxEnergy = maxEnergy-1-(2*c[currentIndex])
        if currentIndex == 0:
            break
    return maxEnergy
print(jumpingOnClouds([0,0,1,0,0,1,1,0]))