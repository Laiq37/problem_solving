def jumpingOnClouds(c):
    i = 0
    minJump = 0
    while True:
        if i+1 >= len(c):
            break
        if i+2 <len(c) and c[i+2] == 0:
            i = i+2
        elif i+1 < len(c) and c[i+1] == 0:
            i = i+1
        minJump+=1
    return minJump
print(jumpingOnClouds([0,1,0,0,1,0]))