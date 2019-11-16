def linearSearch(L, key):

    if len(L) == 0:
        return False
    if L[0] == key:
        return True

    return linearSearch(L[1:],key)

def binarySearch(L, key):

    low  = 0
    high = len(L)
    mid  = (high+low)//2
    
    if len(L) == 0:
        return False
    if L[mid] == key:
        return True
    if L[mid] > key:
        return binarySearch(L[:mid],key)
    if L[mid] < key:
        return binarySearch(L[mid+1:],key)

def BSI(L, key, start, end):

    if start > end:
        return -1

    mid = (start+end)//2

    if L[mid]==key:
        return mid
    elif L[mid]<key:
        return BSI(L, key, start, mid -1)
    elif L[mid]>key:
        return BSI(L,key,start+1,end)
    
def BS(L, key):

    return BSI(L, key, 0, len(L) - 1)

def quickSort(L):

    # base case: 
    if len(L) == 0 or len(L) == 1:
        return L

    # pick a pivot randomly:
    pivot = L.pop(0)

    # Split the list in 2 about the pivot:
    left = []
    right = []
    for e in L:
        if e <= pivot:
            left.append(e)
        else:
            right.append(e)

    # Sort both sublists
    left = quickSort(left)
    right = quickSort(right)

    # Stitch everything back together:

    return left + [pivot] + right

def merge(L1,L2):

    # Create an empty output list:
    result = []
    # While both lists have elements
    while len(L1) != 0 and len(L2) != 0:
        # Compare the irst item of each list
        if L1[0] <= L2[0]:
            result.append(L1.pop(0))
        else:
            result.append(L2.pop(0))
        # Move the smallest of the two into the output

    # one of the lists is empty
    if len(L1) > 0:
        result = result + L1
    else:
        result = result + L2
    # add all of the remaining items to the end of the output

    return result

def mergeSort(L):

    if len(L) == 0 or len(L) == 1: # base case list is small enough to be default sorted
        return L
    
    #split the list in two
    mid = len(L)//2
    left = L[:mid]
    right = L[mid:]
    # sort both halfs
    left = mergeSort(left)
    right = mergeSort(right)
    # merge both sorted sublists

    return merge(left, right)

print(mergeSort([1,2,5,6,88,77,6,4,33,2,44,6666,7,8,9,8,0,888888,765,345,13,146,766,11345]))