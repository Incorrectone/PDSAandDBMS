import random

# Create a random List
l=[]
n=1077
for i in range(n):
    l.append(random.randint(0,100))


lh = [2, 6, 8, 11, 17, 23, 33, 44, 46, 50, 65]

def binarysearch(l, number, i = 1):
    if l == []:
        return (False)
    
    mid_point = len(l) // 2
    
    if l[mid_point] == number:
        return (True)
    
    if l[mid_point] >= number:
        return binarysearch(l[:mid_point], number)
    else:
        return binarysearch(l[mid_point+1:], number)

def binarySearchIndexAndComparisons(l, number, i = 0):
    if l == []:
        return (False, i + 1)
    
    mid_point = (0 + len(l)) // 2
    
    if l[mid_point] == number:
        return (True, i + 1)
    
    if l[mid_point] >= number:
        return binarySearchIndexAndComparisons(l[:mid_point], number, i)
    else:
        return binarySearchIndexAndComparisons(l[mid_point+1:], number, i + 1)

print(binarySearchIndexAndComparisons(lh, 13))
print(binarySearchIndexAndComparisons(lh, 100))

# Merge Sort
def merge(b, h):
    (bp, hp) = (0, 0)
    (m, n) = (len(b), len(h))
    l = []
    for i in range(m + n):
        if bp == m:
            l.extend(h[hp:])
            break
        elif hp == n:
            l.extend(b[bp:])
            break
        elif b[bp] > h[hp]:
            l.append(h[hp])
            hp += 1
        else:
            l.append(b[bp])
            bp += 1
    return l      

def mergesort(l):
    if len(l) <= 1:
        return l
    
    midpoint = len(l) // 2
    bottom_half = mergesort(l[:midpoint])
    top_half = mergesort(l[midpoint:])
    
    return merge(bottom_half, top_half)

print(sorted(l) == mergesort(l))





    