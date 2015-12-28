Python 2.7.8 (v2.7.8:ee879c0ffa11, Jun 29 2014, 21:07:35) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
"""
Sorting Lab
Data Structures cs106
Haverford College

Please complete a sorting function, selecting from
 - SelectionSort(list)
 - InsertionSort(list)
 - BubbleSort(list)
 - HeapSort(list)
 - TreeSort(list) # a.k.a., BSTsort(list)
 - other (get permission!)
Please replace "YourSort" with the name of the sort you chose to implement
Look at the bottom of the file as well!

"""

import sys
import time
import random

def insertionSort(a): #insertion sort
# replace with your sort function
    #a.sort()     # Python built-in sort function !!!!!
    lo = 0           
    i = lo + 1
    b = []
    while lo < a.length:
        if a[i] < a[lo]:
            b.append(a[i])
            lo += 1
        elif a[i] > a[lo]:
            b.append(a[lo])
            lo += 1
    return b
#     hi = len(a)
#     while i < hi:
#         if a[i] > a[lo]:
#             i = lo
#             i += 1
#         elif a[i] < a[lo]:
#             i += 1
#     return a
    

#---------------------------------------------
# code for QuickSort
#
# simple function to exchange a[i] and a[j]
def exch(a, i, j):
    a[i], a[j] = a[j], a[i]
        
# swap around "j" (pivot)
def partition(a, lo, hi):
    i = lo + 1
    j = hi
    while 1:
        while i <= j and a[i] <= a[lo]:
            i += 1
        while i <= j and a[lo] <= a[j]:
            j -= 1
        if i > j:
            break
        exch(a, i, j)
    exch(a, lo, j)
    return j

# recursive run QuickSort on each partition
def quick(a, lo, hi):
    if hi <= lo:
        return
    j = partition(a, lo, hi)
    quick(a, lo, j-1)
    quick(a, j+1, hi)

def quicksort(a):
    random.shuffle(a)
    quick(a, 0, len(a)-1)

#-------------------------------------------

# take partitions assumed sorted and merge
def merge(a, aux, lo, mid, hi):
    for k in range(lo, hi+1):
        aux[k] = a[k]
        i = lo
        j = mid + 1
        for k in range(lo, hi+1):
            if i > mid:
                a[k] = aux[j]
                j += 1
            elif j > hi:
                a[k] = aux[i]
                i += 1
            elif aux[j] < aux[i]:
                a[k] = aux[j]
                j += 1
            else:
                a[k] = aux[i]
                i += 1
# recursive sort each half
def sort(a, aux, lo, hi):
    if hi <= lo:
        return
    mid = lo + (hi-lo)/2
    sort(a, aux, lo, mid)
    sort(a, aux, mid+1, hi)
    merge(a, aux, lo, mid, hi)

def mergesort(a):
    aux = [0] * len(a)
    sort(a, aux, 0, len(a)-1)

#--------------------------------------------
#
# time execution of a sort of size N
#
def TimeSort(N, ThisSort, name):
    original_seq = range(int(N))
    random.shuffle(original_seq)
    seq = list(original_seq)
    # print original sequence if needed
    if N < displayMax:
        print seq
    # apply mergesort
    print 'Running ' + str(name)
    start = time.clock()
    ThisSort(seq)
    end = time.clock()
    # print sorted sequence if needed
    if N < displayMax:
        print "Sorted list:"
        print seq
    print 'Elapsed time:', end-start
    print 'Results correct?', seq==range(N)
    print

#-------------------------------------------
if __name__ == "__main__":
        # generate sequence
        displayMax = 30
        N = int(raw_input("How many integers to sort?: "))
        TimeSort(N, mergesort, "MergeSort")
        TimeSort(N, quicksort, "QuickSort")
        TimeSort(N, insertionSort, "YourSort") #need to change name


