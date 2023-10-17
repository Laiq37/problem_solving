def getDifference(val1,val2):
    return (val1-val2 + abs(val1-val2))//2
def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    if y1 > y2:
        return (y1-y2)*10000
    elif m1 > m2 and y1 >= y2:
        return (m1-m2)*500
    elif d1 > d2 and m1>= m2 and y1 >= y2:
        return (d1-d2)*15
    else:
        return 0
print(libraryFine(2,7,1014,1,2,1015))