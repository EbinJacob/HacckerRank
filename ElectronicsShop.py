#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    # Write your code here.
    n=len(keyboards)
    m=len(drives)
    elem=[]
    flag=0
    temp=0
    for i in range(0,n):
        for j in range(0,m):
            temp=keyboards[i]+drives[j]
            if temp<=b:
                elem.append(temp)
                flag=1
    if flag==0:
        ans=-1
        return ans
    else:
        ans=max(elem)
        return ans
                
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
