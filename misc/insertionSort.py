def insertionSort(ar): 
    s = ar[-1]
    if len(ar)<=1:
        print str(ar)
        return ""
    for i in range(len(ar)-2,-1,-1):
        if ar[i]> s:
            ar[i+1] = ar[i]
            print " ".join(map(str,ar))
            if i ==0:
                ar[i] = s
                print " ".join(map(str,ar))
                return ""
        else:
            ar[i+1] = s
            print " ".join(map(str,ar))
            break
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)

"""
example input from std:

5
1 2 3 4 3

"""
