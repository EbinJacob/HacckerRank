#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    count=0
    n=len(a)
    for i in range (0,n):
        for i in range(1,n):
            if a[i-1]>a[i]:
                temp=a[i-1]
                a[i-1]=a[i]
                a[i]=temp
                count=count+1
    c=str(count)
    print("Array is sorted in "+c+" swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[n-1])
    

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
