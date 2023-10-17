def permutationEquation(p):
    # Write your code here
    y = []
    for i in range(0, len(p)):
        y.append(p[p[i]-1])
    return y
permutationEquation([4, 3, 5, 1 ,2])