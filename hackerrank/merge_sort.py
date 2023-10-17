def merge_sort(n,totalSwap):
    if len(n)<2:
        return [n,0]
    totalSwap = totalSwap
    left = merge_sort(n[0:len(n)//2],totalSwap)
    right = merge_sort(n[len(n)//2:],totalSwap)
    totalSwap += left[1]+right[1]
    li, ri = 0,0
    sortArray = []
    while True:
        if left[0][li] > right[0][ri]:
            sortArray.append(right[0][ri])
            totalSwap += 1
            ri +=1
        elif left[0][li] <= right[0][ri]:
            sortArray.append(left[0][li])
            li +=1
        if li == len(left[0]):
            sortArray = sortArray + right[0][ri:]
            totalSwap += 1
            break
        elif ri == len(right[0]):
            sortArray = sortArray + left[0][li:]
            if(li <= len(left[0][li:])-1):
            #     totalSwap += len(left[0][li+1:])
            # else:
                totalSwap += len(left[0][li:])
            break
    return sortArray,totalSwap

numbers_str = "480130 735329 810013 140187 972418 357056 334780 854684 478980 34590 180238 567090 935248 834854 514996 950881 104525 874212 160000 528785 770712 201115 830644 535327 668785 241043 946633 645108 184097 251762 97219 664226 503442 907232 320764 992211 264287 171895 846895 259618 722836 543484 343059 658083 378338 858054 125316 999214 248618 285315 527999 535681 2781 358642 71007 671565 116036 17639 833024 300132 785753 930243 480710 805546 353826 317825 797757 134464 6072 161003 394081 728907 704486 253492 386990 599175 111545 28657 598389 360162 313971 642739 895842 833103 1380 966849 21019 633767 500839 854043 450251 802943 784285 930960 608489 654462 765136 922597 788925 771207 83599 699357 500114 304436 952848 403455 419963 580745 432111 534703 457258 262433"

# Convert the string of numbers into a list of integers
numbers_list = [int(num) for num in numbers_str.split()]
print(len(numbers_list))

# print(numbers_list)


print(merge_sort(
    numbers_list,0))
    # [7,5,3,2],0))
    # [2, 1 ,3, 1, 2],0))
    # [2,1,10,8, 7, 6,50,9, 100,3, 5,25,18, 17 ,19,13,40,50,38,23],0))