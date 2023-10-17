# def nonDivisibleSubset(k, s):
#     modEle ={}
#     for ele in s:
#         modEle[ele]= ele % k
#     i = 0
#     j = 1
#     while True:
#         if len(s)-1 == i:
#             break
#         elif len(s)<= j:
#             i +=1
#             j = i+1 
#         elif modEle[s[i]] + modEle[s[j]] == k or modEle[s[i]] + modEle[s[j]] ==0:
#             s.remove(s[j])
#         else:
#             j+=1
#     return len(s)
def nonDivisibleSubset(k, s):
    remainders = [0]*k
    for ele in s:
        remainders[ele % k] += 1
    maxDivSubsetLen = 0
    if remainders[0] > 0:
        maxDivSubsetLen +=1
    for i in range(1, len(remainders)):
        if i > len(remainders)-i:
            break
        elif i == len(remainders)-i:
            if remainders[i] >0:
                maxDivSubsetLen += 1
            break
        if remainders[i] > remainders[len(remainders)-i]:
            maxDivSubsetLen += remainders[i]
        else:
            maxDivSubsetLen += remainders[len(remainders)-i]
        if i > len(remainders)-i:
            break
    return maxDivSubsetLen
            
# print(nonDivisibleSubset(3,[1,7,2,4]))
print(nonDivisibleSubset(7,[278,576,496,727,410,124,338,149,209,702,282,718,771,575,436]))
# print(nonDivisibleSubset(4,[19,10,12,10,24,25,22]))