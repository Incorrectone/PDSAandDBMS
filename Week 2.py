import random

# Create a random List
l=[]
n=1077
for i in range(n):
    l.append(random.randint(0,100))
    
def Cloning(li1):
    li_copy = li1[:]
    return li_copy

G = Cloning(l)

def quicksort(L):
    if len(L) <= 1:
        return L
    
    pivot = L[0]
    
    (upper, lower) = (0, 0)
    
    for i in range(0, len(L)):
        if L[i] > pivot:
            upper += 1
        else:
            (L[i], L[lower-1]) = (L[lower-1], L[i])
            (upper, lower) = (upper + 1, lower + 1)
    (L[0], L[lower - 1])= (L[lower - 1], L[0])
    lower = lower - 1 
    quicksort(L[0:lower])
    quicksort(L[lower + 1: upper])
    
    return L

print(quicksort(l))